# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:53:47 2021

@author: db_wi
"""

def euler016():
    a = str(2**1000)
    r = 0
    for i in a:
        r += int(i)
    return r