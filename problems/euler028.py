# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:17:46 2021

@author: db_wi
"""

def euler028():
    width = 1001
    r = 1
    it = 1
    w = 2
    while w <= width:
        for i in range(4):
            it += w
            r += it
        w += 2
    return r