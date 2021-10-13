# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:06:08 2021

@author: db_wi
"""

def euler052():
    def counts(n):
        f = str(n)
        l = [ 0 for x in range(10) ]
        for i in f:
            l[int(i)] += 1
        return ''.join([str(i) for i in l])
    x = 10
    s = 10
    f = 17
    while True:
        cnts = counts(x)
        found = True
        for i in range(2,7):
            if not counts(x*i) == cnts:
                found = False
                break
        if not found:
            x += 1
            if x == f:
                f = (f-1)*10 + 7
                s *= 10
                x = s
        else:
            return x