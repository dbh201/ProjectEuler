# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:42:48 2021

@author: db_wi
"""

def euler004():
    r = -1
    for a in range(999,99,-1):
        for b in range(a,99,-1):
            candidate = a*b
            if candidate < r:
                break
                    
            if test_palindrome(str(candidate)):
                r = candidate
    return r