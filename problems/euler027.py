# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:00:59 2021

@author: db_wi
"""

def euler027():
    max_n = 0
    retval = None
    for a in range(-999,1000):
        for b in range(-999,1000):
            n = 0
            r = n**2 + a*n + b
            if r < 2:
                continue
            while PRIME_DB.check_prime(r):
                n += 1
                r = n**2 + a*n + b
                if r < 2:
                    break
            if n > max_n:
                #print("Found a=%i,b=%i" % (a,b))
                max_n = n
                retval = a*b
    return retval