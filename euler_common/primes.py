# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 19:00:02 2021

@author: db_wi
"""
import struct

# H = unsigned short, little endian
import logging
class PrimeDB():
    FMT_64LE_FILENAME = "primes64le.bin"
    FMT_MIXED_FILENAME = "primes_mixed_le.bin"
    FMT_8LE  = "<B"
    FMT_16LE = "<H"
    FMT_32LE = "<I"
    FMT_64LE = "<Q"
    FMT_SWITCH_CODES = {
        1: (FMT_16LE,2),
        2: (FMT_32LE,4),
        4: (FMT_64LE,8)
        }
    
    def __init__(self,prime_count=None,max_prime=None):
        self.db = list()
        self.set = set()
        self._max_prime_in_db = 0
        self._disable_saving = False
        
    def _try_load(self,prime_count=None,max_prime=None):
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
                        
                self.set = set(self.db)
                self._max_prime_in_db = self.db[-1]
                
        except FileNotFoundError:
            logging.warn("database file not found, rebuilding...")
            self._rebuild_db()
        
    def _update_db_mixed(self):
        if self._disable_saving:
            logging.warning("System cannot save new primes at this time! Please check logs.")
            return
        with open(self.FMT_MIXED_FILENAME,"wb") as f:
            fmt = self.FMT_8LE
            fmt_len = 1
            index_to_start = self.db.rindex(self._max_prime_in_db)
            try:
                idx = index_to_start + 1
                try:
                    while True:    
                        # Get smallest applicable format tuple
                        while self.db[idx] > 256**fmt_len:
                            fmt,fmt_len = self.FMT_SWITCH_CODES[fmt_len]
                        # Bulk write the subset of primes which can be written in this format
                        while self.db[idx] <= 256**fmt_len:
                            idx += 1
                        f.write(struct.pack(fmt,self.db[index_to_start+1:idx]))
                        f.write(struct.pack(fmt,(0,fmt_len)))
                        index_to_start=idx
                        fmt,fmt_len = self.FMT_SWITCH_CODES[fmt_len]
                except IndexError:
                    f.write(struct.pack(fmt,self.db[index_to_start:]))
                    
            except KeyError:
                logging.error("Unable to save prime to file: No suitable format for %i (too large!)" % self.db[idx])
            self._max_prime_in_db = self.db[-1]
                
    def _rebuild_db(self):
        urlstr = "https://primes.utm.edu/lists/small/millions/primes%i.zip"
        dirstr = "primezips/"
        zipstr = "primes%i.zip"
        txtstr = "primes%i.txt"
        i = 1
        while i < 51:
            try: 
                with open(dirstr + txtstr % i, "r") as txt:
                    for line in txt.readlines()[1:]:
                        for prime in line.split(" "):
                            try:
                                self.db.append(int(prime))
                            except ValueError:
                                continue
                    i += 1
            except FileNotFoundError:
                try:
                    import zipfile
                    with zipfile.ZipFile(dirstr + zipstr % i) as unzip:
                        with open(dirstr + txtstr % i,"wb") as txt:
                            txt.write(unzip.read(txtstr % i))
                except FileNotFoundError:
                    import requests
                    url = urlstr % i
                    print("Downloading " + url)
                    r = requests.get(url)
                    with open(dirstr + zipstr % i,"wb") as w:
                        w.write(r.content)
        self.set = set(self.db)
                        
                    
                

    def is_prime(self,n):
        if n > self.db[-1]:
            self._extend_to(n)
        return n in self.set
    
    def _check_if_prime(self,i):
        prime = True
        for j in self.db:
            if i%j == 0:
                prime = False
                break
            if j*j > i:
                break
        return prime
    
    def _find_next_prime(self):
        i = self.db[-1] + 2
        if self._check_if_prime(i):
            self.db.append(i)
            self.set.add(i)
            return
        i += 2
            
    def _extend_to(self,target):
        """extend the database until it reaches or passes the target number"""
        while self.db[-1] < target:
            self._find_next_prime()
    
    def _extend_until(self,amount):
        """extend the database until it has this amount of entries"""
        while len(self.set) < amount:
            self._find_next_prime()
    
    def _extend_by(self,count):
        """extend the database by a certain amount of primes"""
        while count > 0:
            self._find_next_prime()
            count -= 1
            