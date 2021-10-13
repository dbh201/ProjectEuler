# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:19:03 2021

@author: db_wi
"""

def euler057():
    def get_root_2_fraction_terms(n,d):
        t = n
        n = d
        d = t
        d += n
        n += d
        return (n,d)
    n = 1
    d = 1
    r = 0
    for i in range(1000):
        n,d = get_root_2_fraction_terms(n,d)
        if len(str(n)) > len(str(d)):
            r += 1
    return r
