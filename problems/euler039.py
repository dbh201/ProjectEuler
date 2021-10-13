# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:27:55 2021

@author: db_wi
"""

def euler039():
    # right angle triangle
    # the two other angles must add up to 90
    # all three sides must be integral to be considered a solution
    # which value of p <= 1000 has the most solutions?

    # my man pythagoras gonna hook me up
    # a^2 + b^2 = c^2
    # a < c
    # b < c
    # a + b + c = p

    # This is a brutally brute force attack on math
    # This takes way too long, too...
    # I refuse to use sqrt(). This can be solved without it.
    perms = dict()
    for a in range(1,1001):
        for b in range(a,1001):
            csq = a*a + b*b
            c = b + 1
            while csq > c*c:
                c += 1
            p = a + b + c
            if p > 1000:
                break
            if not a*a + b*b == c*c:
                continue
            
            if not p in perms:
                perms[p] = 1
            else:
                perms[p] += 1
    m = 0
    mp = 0
    for key,val in perms.items():
        if val > m:
            m = val
            mp = key
    return mp