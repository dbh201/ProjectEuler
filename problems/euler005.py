# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:44:05 2021

@author: db_wi
"""

def euler005():
    primes = [2,3,5,7,11,13,17,19]
    # Prime factors - we're going to reconstruct the number
    # by figuring out which prime factors we need, and how many
    pfs = [0,0,0,0,0,0,0,0]

    # scan the numbers as required by the question
    for i in range(20,1,-1):
        # check their prime factors
        for j in range(len(primes)):
            k = 0
            l = i
            while not (l%primes[j]):
                l //= primes[j]
                k +=  1
            # keep track of how many we need, at maximum
            if k > pfs[j]:
                pfs[j] = k

    # reconstruct number
    r = 1
    for i in range(len(primes)):
        r *= primes[i]**pfs[i]

    return r