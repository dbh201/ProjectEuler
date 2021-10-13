# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:10:23 2021

@author: db_wi
"""

def euler056():
    r = 0
    for a in range(1,101):
        for b in range(1,101):
            i = 0
            for c in str(pow(a,b)):
                i += int(c)
            if i > r:
                r = i
    return r