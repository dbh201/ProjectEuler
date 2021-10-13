# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:18:57 2021

@author: db_wi
"""

def euler029():
    terms = set()
    for a in range(2,101):
        for b in range(2,101):
            if not a**b in terms:
                terms.add(a**b)
    return len(terms)