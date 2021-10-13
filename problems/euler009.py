# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:46:20 2021

@author: db_wi
"""

def euler009():
    for a in range(1,1001):
        for b in range(a+1,1001):
            c_sq = a**2 + b**2
            if not c_sq == (1000 - a - b)**2:
                continue
            return a*b*(1000-a-b)