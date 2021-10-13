# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:41:18 2021

@author: db_wi
"""

def euler046():
    i = 7
    found = False
    while not found:
        i += 2
        if PRIME_DB.check_prime(i):
            continue
        is_goldbach = False
        for prime in PRIME_DB.db:
            if prime >= i:
                break
            test = i - prime
            # while test > sqmax:
            #     sqidx += 1
            #     sqmax = 2*sqidx*sqidx
            #     sqset.add(sqmax)
            test //= 2
            sq = 1
            while sq*sq < test:
                sq += 1
            if sq*sq == test:
                is_goldbach = True
                break
            
            #if test in sqset:
            #    is_goldbach = True
            #    break
            
        if not is_goldbach:
            return i