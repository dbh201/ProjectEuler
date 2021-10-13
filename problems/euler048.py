# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:44:24 2021

@author: db_wi
"""

def euler048():
    s = 0
    for i in range(1,1001):
        s += (i**i) % (10**10)
        s %= (10**10)
    return s