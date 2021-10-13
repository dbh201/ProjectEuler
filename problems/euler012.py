# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:52:39 2021

@author: db_wi
"""
def euler012():
    # starting triangle number
    tri = TriangleNumberSequence()
    i = 1
    d = 1
    while d < 500:
        i += 1
        d = len(PRIME_DB.get_divisors(tri.get_nth(i)))
    return tri.get_nth(i)