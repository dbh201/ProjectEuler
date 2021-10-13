# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:36:14 2021

@author: db_wi
"""

def euler063():
    done = False
    i = 1
    p = 1
    c = 0
    cip = 0
    while not done:
        s = str(i**p)
        if len(s) > p:
            if cip == 0:
                break
            p += 1
            i = 1
            c += cip
            cip = 0
        elif len(s) == p:
            cip += 1
            i += 1
        else:
            i += 1
    return c
