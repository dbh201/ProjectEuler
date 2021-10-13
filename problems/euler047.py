# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:43:33 2021

@author: db_wi
"""

def euler047():
    found = False
    i = 10

    consecutive_length = 0
    contest = 2
    while not found:
        itest = i
        fset = set()
        for piter in PRIME_DB.db:
            while not itest % piter:
                fset.add(piter)
                itest //= piter
            if itest == 1 or piter > i*2:
                break
        if len(fset) == contest:
            consecutive_length += 1
            if consecutive_length == contest:
                if contest == 4:
                    found = True
                    return i-3
                contest += 1
        else:
            consecutive_length = 0
        i += 1