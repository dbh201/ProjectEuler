# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:53:23 2021

@author: db_wi
"""

def euler014():
    md = 0
    mn = 0
    chains = dict()
    for m in range(1,1000000,1):
        d = 0
        chain = []
        n = m
        while n > 1:
            chain.append(n)
            if n in chains and chains[n] > 0:
                d += chains[n]
                break
            if (n%2):
                n = (n*3) + 1
            else:
                n = n//2
            d += 1
        chain.append(1)
        for c in range(len(chain)):
            if not chain[c] in chains:
                chains[chain[c]] = len(chain)-c
        if d > md:
            md = d
            mn = m
    return mn