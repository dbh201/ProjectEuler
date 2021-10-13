# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:22:28 2021

@author: db_wi
"""

def euler034():
    # find maximum
    FACS = dict()
    FACS[0] = 1
    for i in range(1,10):
        FACS[i] = i * FACS[i-1]
    x = 1
    limit = FACS[9]
    while 10**x < limit:
        x += 1
        limit += FACS[9]
    retval = 0
    for i in range(3,limit):
        a = sum([FACS[int(l)] for l in str(i)])
        if a == i:
            retval += a
    return retval