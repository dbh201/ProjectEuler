# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:56:50 2021

@author: db_wi
"""

def euler023():
    abundant = set([12,18])
    r = 171
    for i in range(19,28124):
        isd = sum(PRIME_DB.get_proper_divisors(i))
        if isd > i:
            abundant.add(i)
        add_to_result = True
        for a in abundant:
            if (i-a) in abundant:
                add_to_result = False
                break
        if add_to_result:
            r += i
    return r