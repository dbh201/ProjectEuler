# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:39:29 2021

@author: db_wi
"""

def euler045():
    tria = TriangleNumberSequence()
    pent = PentagonalNumberSequence()
    hexa = HexagonalNumberSequence()
    ti = 285
    tn = tria.get_nth(ti)
    pi = 165
    pn = pent.get_nth(pi)
    hi = 143
    hn = hexa.get_nth(hi)
    found = False
    while not found:
        hi += 1
        hn = hexa.get_nth(hi)
        while(pn < hn):
            pi += 1
            pn = pent.get_nth(pi)
        if pn > hn:
            continue
        while(tn < hn):
            ti += 1
            tn = pent.get_nth(ti)
        if tn > hn:
            continue
        found = True
    return tn