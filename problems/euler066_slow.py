# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:24:29 2021

@author: db_wi
"""

# Way too slow
def euler066():
    x_largest = 0
    D_ret = 0
    for D in range(2,1001):
        if int(sqrt(D))**2 == D:
            continue
        y = 2
        while True:
            x_sq = 1 + D*y*y
            x = sqrt(x_sq)
            if int(x)**2 == x_sq:
                if x_largest < x:
                    x_largest = x
                    D_ret = D
                    break
            y += 1
    return D_ret