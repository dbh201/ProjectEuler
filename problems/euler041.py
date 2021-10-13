# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:28:36 2021

@author: db_wi
"""

def euler041():
    m = 2143
    fac = FactorialSequence()
    for n in range(4,10):
        a = [ x for x in range(1,n+1) ]
        if a[-1] % 2 == 0:
            continue
        for i in range(fac.get_nth(len(a))):
            b = permute(i,a)
            s = ""
            for j in b:
                s += str(j)

            if PRIME_DB.check_prime(int(s)):
                m = int(s)
    return m