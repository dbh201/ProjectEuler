# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:39:40 2021

@author: db_wi
"""

def euler044():
    pent_list = set()
    pent = PentagonalNumberSequence()
    max_pent = pent.get_nth(2)
    max_n = 2
    pent_list.add(pent.get_nth(1))
    pent_list.add(max_pent)
    found = False
    i = 2
    D = 0
    while not found:
        pk = pent.get_nth(i)
        i += 1
        D = pk
        while max_pent < (pk*2):
            max_n += 1
            max_pent = pent.get_nth(max_n)
            pent_list.add(max_pent)
        for pj in pent_list:
            if pj >= pk:
                continue
            if (pk - pj) in pent_list:
                if (pj + pk) in pent_list and D > (pk-pj):
                    D = pk-pj
                    found = True
    return D