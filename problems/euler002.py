# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:31:32 2021

@author: db_wi
"""
def euler002():
    a = FibonacciSequence()
    r = 0
    i = 0
    n = 0
    while i < 4000000:
        i = a.get_nth(n)
        if not (i%2):
            r += i
        n += 1
    return r