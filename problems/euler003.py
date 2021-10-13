# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:42:10 2021

@author: db_wi
"""

def euler003():
    lpf = 600851475143
    # This is a bit brute-force... 
    a = PRIME_DB.get_prime_list(max_prime=1000000)
    r = -1
    for i in a:
        while not (lpf % i):
            lpf = lpf//i
            r = i
        if lpf == 1:
            break
    return r