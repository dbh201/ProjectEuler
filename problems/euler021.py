# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:54:55 2021

@author: db_wi
"""

def euler021():
    proper_divisors = dict()
    r = 0
    for i in range(2,10000):
        if not i in proper_divisors:
            ipd = PRIME_DB.get_proper_divisors(i)
            proper_divisors[i] = sum(ipd)
            j = proper_divisors[i]
            if j == i:
                continue
            if not j in proper_divisors:
                jpd = PRIME_DB.get_proper_divisors(j)
                proper_divisors[j] = sum(jpd)
            if proper_divisors[j] == i:
                r += proper_divisors[i] + proper_divisors[j]
    return r