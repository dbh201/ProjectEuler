# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:20:12 2021

@author: db_wi
"""

def euler032():
    products = set()
    
    def test(a,b):
        s = str(a) + str(b) + str(a*b)
        if len(s) != 9:
            return False
        for i in range(1,10):
            if s.count(str(i)) != 1:
                return False
        return True

    for a in range(1,10):
        for b in range(1000,10000):
            if test(a,b) and a*b not in products:
                products.add(a*b)
                
    for a in range(10,100):
        for b in range(100,1000):
            if test(a,b) and a*b not in products:
                products.add(a*b)
    return sum(products)