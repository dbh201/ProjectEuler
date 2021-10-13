# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:57:56 2021

@author: db_wi
"""

def euler025():
    l = [1,1]
    while len(str(l[-1])) < 1000:
        l.append(l[-2]+l[-1])
    return len(l)