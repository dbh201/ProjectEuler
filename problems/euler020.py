# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:54:43 2021

@author: db_wi
"""

def euler020():
    f = 1
    for i in range(1,101):
        f = f*i
        
    r = 0
    for i in str(f):
        r += int(i)
    return r