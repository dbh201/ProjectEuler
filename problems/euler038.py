# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:26:58 2021

@author: db_wi
"""

def euler038():
    m = 918273645
    i = 0
    def iterate(inp):
        i = inp + 1
        if str(i)[0] != '9':
            i = int("9" + str(i))
        return i
            
    while i < 99999:
        s = str(i)
        j = 2
        while len(s) < 9:
            s += str(i*j)
        if int(s) > m and test_pandigital(s):
            m = int(s)
        i = iterate(i)
    
    return m  