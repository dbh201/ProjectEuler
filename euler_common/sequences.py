# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 18:54:30 2021

@author: db_wi
"""

def get_nth_triangle_number(n):
    return n*(n+1)//2
def get_nth_square_number(n):
    return n*n
def get_nth_pentagon_number(n):
    return n*((3*n)-1)//2
def get_nth_hexagonal_number(n):
    return n*((n*2)-1)
def get_nth_heptagonal_number(n):
    return n*((5*n)-3)//2
def get_nth_octagonal_number(n):
    return n*((3*n)-2)
def get_nth_factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n*get_nth_factorial(n-1)



def generate_fibonacci_sequence(n, limit=False, pregen=None):
    if pregen:
        fibs = pregen
    else:
        fibs = [0,1]
        
    if limit:
        i = len(fibs)
        while True:
            f = fibs[i-1]+fibs[i-2]
            if f < n:
                fibs.append(f)
                i += 1
            else:
                break
    else:
        for i in range(len(fibs),n+1):
            f = fibs[i-1]+fibs[i-2]
            fibs.append(f)
            
    return fibs