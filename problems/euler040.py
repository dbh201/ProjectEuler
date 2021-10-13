# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:28:10 2021

@author: db_wi
"""

def euler040():
    s = "."
    n = 1
    while(len(s) <= 1000000):
        s += str(n)
        n += 1
    r = 1
    #print(s[12])
    #print(s[11])
    #print(s[10])
    #print(s[9])
    #print(len(s))
    #print(n)
    for i in range(7):
        #print("r: %i * %i (s[%i])" % (r,int(s[10**i]),10**i))
        r *= int(s[10**i])
    return r