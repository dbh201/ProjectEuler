# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 19:00:02 2021

@author: db_wi
"""

import zipfile
import logging
import os
from math import sqrt
from itertools import combinations


STARTING_PRIMES = 1000000
#TODO: make a quick-loading binary prime database file!
#from euler_common.primefile import IntegerDBFile
class PrimeDB():
    DEFAULT_DB_FILE = "primes_mixed_le.bin"
    PRIMES_IN_TXTFILES = 50000000
    PRIMES_PER_FILE = 1000000 
    def __init__(self,initial_size=None,last_prime_gt=None):
        self.log = logging.getLogger(__name__)
        self.db = list()
        self.set = set()
        self._max_prime_in_db = 0
        self._disable_saving = False
        self._initialise_db(initial_size,last_prime_gt)
                
    def _initialise_db(self,initial_size,last_prime_gt):
        self.set.clear()
        self.db.clear()
        self._load_from_files(db_target_size=initial_size)
        
    def _load_from_files(self,db_target_size=None,db_target_prime=None):
        urlstr = "https://primes.utm.edu/lists/small/millions/primes%i.zip"
        dirstr = "primezips/"
        zipstr = "primes%i.zip"
        txtstr = "primes%i.txt"
        i = 1
        db_orig_size = len(self.db)
        primes_read = 0
        finished = False
        while i < 51:
            try:
                # is the text file available? if so, load all of the prime
                # string tokens, parse them to int and add them to the list
                with open(os.path.join(dirstr,txtstr % i), "r") as txt:
                    for line in txt.readlines()[1:]:
                        p = line.strip().split(" ")
                        primes = list()
                        for j in p:
                            if j == "": continue
                            primes.append(int(j))
                        if len(primes) > 0:
                            try:
                                for prime in primes:
                                    finished = False
                                    if db_target_size:
                                        if primes_read + db_orig_size >= db_target_size:
                                            finished = True
                                        else:
                                            finished = False
                                    if db_target_prime:
                                        if self.db[-1] >= db_target_prime:
                                            finished = True
                                        else:
                                            finished = False
                                    if finished:
                                        break
                                    self.db.append(prime)
                                    primes_read += 1
                            except ValueError:
                                continue
                    if finished:
                        break
                    i += 1
            except FileNotFoundError:
                # text file was not available - try unzipping it from the zipfile
                try:
                    with zipfile.ZipFile(os.path.join(dirstr,zipstr % i)) as unzip:
                        with open(os.path.join(dirstr,txtstr % i),"wb") as txt:
                            txt.write(unzip.read(txtstr % i))
                
                # zipfile was not available - try to download it, then restart the loop
                except FileNotFoundError:
                    import requests
                    url = urlstr % i
                    self.log.info("Downloading " + url)
                    r = requests.get(url)
                    with open(dirstr + zipstr % i,"wb") as w:
                        w.write(r.content)
                        
        # once every prime is loaded, create a memory set for easy testing
        self.set = set(self.db)
                        
                    
                
    def check_prime(self,n):
        if n < self.db[-1]:
            return n in self.set
        return self._check_if_prime(n)
    
    def is_prime(self,n):
        if n > self.db[-1]:
            self._extend_to(n)
        return n in self.set
    
    def is_prime_slow(self,n):
        for i in self.db:
            if i*i > n:
                return True
            if not n%i:
                return False
    def get_nth(self,n):
        self._extend_until(n)
        return self.db[n-1]
    def get_prime_factors(self,n):
        r = []
        for p in self.db:
            if p > n:
                break
            while not n%p:
                n //= p
                r.append(p)
        return r
    
    def get_divisors(self,n):
        if n == 0:
            return None
        pfs = self.get_prime_factors(n)
        r = set()
        for l in range(len(pfs)+1):
            for combos in combinations(pfs,l):
                x = 1
                for c in combos:
                    x *= c
                r.add(x)
        return sorted(list(r))
    
    def get_proper_divisors(self,n):
        return self.get_divisors(n)[:-1]
    
    def _check_if_prime(self,i):
        if self.db[-1]**2 < i:
            self.log.info("db too small to manually test %i, extending...")
            self._extend_to(int(sqrt(i))+2)
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
        
    def get_prime_list(self,max_prime=None,prime_count=None):
        """ Returns a subset of the database of primes, starting at index 0,
        which meets the argument criteria.
        If neither max_prime nor prime_count are set, return a copy of the full
        database.
        If max_prime is set, the list will include all primes below max_prime.
        If prime_count is set, the list will include that amount of primes, in
        order.
        If both are set, the list will contain all primes below max_prime, but
        also include primes above or including max_prime if prime_count was 
        not reached. """
        return_pos = len(self.db)
        if max_prime:
            if max_prime > self.db[-1]:
                self._extend_to(max_prime)
                return_pos = len(self.db)
            else:
                # binary sort to find the pos of the closest prime to max_prime
                pos = len(self.db)//2
                slc = pos//2
                finished = False
                while not finished:
                    if self.db[pos] < max_prime:
                        #print("Position too low (%i), slicing up by %i" % (self.db[pos],slc))
                        pos = pos + slc
                        if slc % 2 == 1:
                            slc += 1
                        slc //= 2
                    elif self.db[pos] > max_prime:
                        #print("Position too high (%i), slicing down by %i" % (self.db[pos],slc))
                        pos = pos - slc
                        if slc % 2 == 1:
                            slc += 1
                        slc //= 2
                    else:
                        return_pos = pos
                        break
                    if slc == 1:
                        if self.db[pos] < max_prime and self.db[pos+1] > max_prime:
                            return_pos = pos + 1
                            finished = True
                    if slc == 0:
                        self.log.warning("Binary slicing width reduced to zero\nUnsure about results...")
                        return_pos = pos
                        finished = True
        if prime_count:
            if prime_count > len(self.db):
                self._extend_until(prime_count)
            if max_prime:
                if return_pos < prime_count:
                    return self.db[:prime_count]
                else:
                    return self.db[:return_pos]
            return self.db[:prime_count]
        else:
            return self.db[:return_pos]
        
            
    def _extend_to(self,target):
        """extend the database until it reaches or passes the target number"""
        if self.db[-1] >= target:
            return
        # load 1 full file at a time until out of files or target passed
        while len(self.db) < self.PRIMES_IN_TXTFILES:
            self._load_from_files(
                self.PRIMES_PER_FILE*((len(self.db)+self.PRIMES_PER_FILE)//self.PRIMES_PER_FILE)
                )
            if self.db[-1] >= target:
                return
        self.log.warning("Exhausted precalculated primes (%i) - manually extending db to primes below %i" % (len(self.db),target))
        while self.db[-1] < target:
            self._find_next_prime()
    
    def _extend_until(self,amount):
        """extend the database until it has this amount of entries"""
        if len(self.set) >= amount:
            return
        if len(self.set) < self.PRIMES_IN_TXTFILES:
            self._load_from_files(amount)
        self.log.warning("Exhausted precalculated primes (%i) - manually extending db until size %i" % (len(self.db),amount))
        while len(self.set) < amount:
            self._find_next_prime()
            
            

try:
    global PRIME_DB
    PRIME_DB
except NameError:
    PRIME_DB = PrimeDB(STARTING_PRIMES)