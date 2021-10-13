# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:57:27 2021

@author: db_wi
"""

def euler024():
    return int(''.join([str(x) for x in permute(1000000-1,[0,1,2,3,4,5,6,7,8,9])]))