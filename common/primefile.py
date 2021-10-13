# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 08:46:30 2021

@author: db_wi
"""
import struct
import logging

# quick binary-encoded database file for integers
#TODO: Decide between monolithic file with multiple integer sizes (16,32,64)
# or separate files. (Separate files are probably easily loaded)
class IntegerDBFile():
    HEADER_UNPACK_STR = "<Q<Q<Q"
    HEADER_DWORD_OFFSET = 8
    HEADER_QWORD_OFFSET = 16
    FMT_8LE  = "<B"
    FMT_16LE = "<H"
    FMT_32LE = "<I"
    FMT_64LE = "<Q"
    FMT_SWITCH_CODES = {
        1: (FMT_16LE,2),
        2: (FMT_32LE,4),
        4: (FMT_64LE,8)
        }
    
    def __init__(self,filename):
        logging.error("IntegerDBFile class TBI!")
        raise Exception("IntegerDBFile class TBI!")
        self._load_metadata(filename)
        
    def _load_metadata(self,filename):
        try:
            with open(filename,"rb") as file:
                self.total_nums, self.dword_offset, self.qword_offset = struct.unpack(self.HEADER_UNPACK_STR,file.read(24))
                if self.total_nums != self.hwords + self.words + self.dwords + self.qwords:
                    logging.error("Header verification failed. Stats read:")
                    logging.error("8bit: %i 16bit: %i 32bit: %i 64bit: %i" %(self.hwords,self.words,self.dwords,self.qwords))
                    logging.error("Total: %i Aggregate: %i")
        except:
            pass
        
    def _load_primes(self,prime_count=None,max_prime=None,verify=False):
        if prime_count and max_prime:
            logging.warning("PrimeDB set with a count of primes and a max prime - will meet both criteria")
        try:
            with open("primes_mixed_le.bin","rb") as f:
                fmt = self.FMT_8LE
                fmt_len = 1
                READ_SWITCH_CODE_NEXT = False
                finished = False
                while not finished:
                    n = f.read(fmt_len)
                    if len(n) == fmt_len:
                        i = struct.unpack(fmt,n)[0]
                        if i == 0:
                            READ_SWITCH_CODE_NEXT = True
                            continue
                        else:
                            if READ_SWITCH_CODE_NEXT:
                                if i in self.FMT_SWITCH_CODES:
                                    READ_SWITCH_CODE_NEXT = False
                                    fmt=self.FMT_SWITCH_CODES[i][0]
                                    fmt_len=self.FMT_SWITCH_CODES[i][1]
                                else:
                                    logging.error("Switch code not implemented: %i" % i)
                                    logging.warning("Last prime was: %i" % self.db[-1])
                                    logging.warning("Unable to read any more primes from file - finishing up.")
                                    self._disable_saving = True
                                    finished = True
                            else:
                                if i in self.set:
                                    continue
                                if verify:
                                    if i > self._max_prime_in_db:
                                        break
                                    print("%i wasn't in db" % i)
                                    self.db.append(i)
                                    self.set.add(i)
                                    continue
                                else:
                                    self.db.append(i)
                                    
                                finished = True
                                if max_prime and self.db[-1] < max_prime:
                                    finished = False
                                if prime_count and len(self.db) < prime_count:
                                    finished = False
                    elif len(n) > 0:
                        logging.warning("Extra data at end of database file...")
                        logging.warning("Final bytes read: %s" % n)
                    else:
                        finished = True
                if verify:
                    self.db.sort()    
                self.set = set(self.db)
                self._max_prime_in_db = self.db[-1]
        except FileNotFoundError:
            logging.error("Database file not found. Please rebuild.")
                
    def _update_db_mixed(self):
        if self._disable_saving:
            logging.warning("System cannot save new primes at this time! Please check logs.")
            return
        with open(self.FMT_MIXED_FILENAME,"ab") as f:
            fmt = self.FMT_8LE
            fmt_len = 1
            try:
                index_to_start = self.db.index(self._max_prime_in_db)
            except ValueError:
                logging.warning("max prime %i was not found in db. Doing a full rebuild...")
                # if we get here, we need to rewrite the whole database
                index_to_start = -1
            try:
                idx = index_to_start + 1
                try:
                    while True:    
                        # Get smallest applicable format tuple
                        while self.db[idx] > 256**fmt_len:
                            fmt,fmt_len = self.FMT_SWITCH_CODES[fmt_len]
                        # Bulk write the subset of primes which can be written in this format
                        while self.db[idx] < 256**fmt_len:
                            idx += 1
                        fullfmt = fmt * (idx-(index_to_start+1))
                        f.write(struct.pack(fullfmt,self.db[index_to_start+1:idx]))
                        f.write(struct.pack(fmt,(0,fmt_len)))
                        index_to_start=idx
                        fmt,fmt_len = self.FMT_SWITCH_CODES[fmt_len]
                except IndexError:
                    if index_to_start == -1:
                        index_to_start = 0
                    f.write(struct.pack(fmt,self.db[index_to_start:]))
                    
            except KeyError:
                logging.error("Unable to save prime to file: No suitable format for %i (too large!)" % self.db[idx])
            self._max_prime_in_db = self.db[-1]
            