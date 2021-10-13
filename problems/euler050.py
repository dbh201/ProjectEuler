# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:51:18 2021

@author: db_wi
"""

def euler050():
    plist = PRIME_DB.get_prime_list(max_prime=1000000)
    l = len(plist)
    p = sum(plist)
    while p > 1000000:
        p -= plist[l-1]
        l -= 1
    while l > 0:
        orig = p
        for i in range(len(plist)-l):
            test = p - plist[i] + plist[l+i]
            if test > 1000000:
                break
            p = test
        if PRIME_DB.check_prime(p):
            return p
        p = orig - plist[l-1]
        l -= 1