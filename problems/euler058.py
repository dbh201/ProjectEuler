# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:19:22 2021

@author: db_wi
"""

def euler058():
    global PRIME_DB
    p = 0
    nums = 1
    n = 1
    it = 0
    done = False
    while not done:
        it += 2
        for i in range(4):
            nums += 1
            n += it
            if PRIME_DB.check_prime(n):
                p += 1
        if p / nums < 0.1:
            done = True
    return it+1