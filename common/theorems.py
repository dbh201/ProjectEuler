# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 09:57:44 2021

@author: db_wi
"""

from math import sqrt
def quadratic_theorem(a,b,c):
    try:
        determinant = sqrt(b**2 - (4*a*c))
    except ValueError:
        return None
    return (-b - determinant)/(2*a), (-b + determinant)/(2*a)