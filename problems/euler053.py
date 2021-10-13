# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:06:37 2021

@author: db_wi
"""

def euler053():
    vs = 1
    vf = 1
    c = 0
    for n in range(1,101):
        vs = n
        rs = 1
        while vs <= 1000000 and rs < n:
            vs *= (n - rs)
            rs += 1
            vs //= rs

        vf = n
        rf = n - 1
        while vf <= 1000000 and rf > 0:
            vf *= rf
            rf -= 1
            vf //= (n-rf)
            
        if rf >= rs:
            c += (rf - rs + 1)    
    return c