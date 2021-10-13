# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:54:27 2021

@author: db_wi
"""

def euler019():
    r = 0
    for year in range(1901,2001):
        for month in range(12):
            d = datetime.date(year,month+1,1)
            if d.weekday() == 6:
                r += 1
    return r