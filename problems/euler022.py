# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:55:57 2021

@author: db_wi
"""

def euler022():
    with open("static/p022_names.txt") as file:
        namelist = list(map(lambda inp: inp.strip('"'),file.read().split(',')))
        
        namelist.sort()
        r = 0
        for name_idx in range(len(namelist)):
            cl = 0
            for c in namelist[name_idx]:
                cl += ord(c) - ord('A') + 1
            cl *= (name_idx+1)
            r += cl
        return r