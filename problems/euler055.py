# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:08:48 2021

@author: db_wi
"""

def euler055():
    count = 0
    for i in range(1,10000):
        if test_lychrel(i):
            count += 1
    return count