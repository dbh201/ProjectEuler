# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:53:35 2021

@author: db_wi
"""

def euler015():
    # to answer this question, we reframe it to:
    # "how many ways are there to get to this point, several layers down,
    # if each point in each layer has 1 or 2 paths leading to it?"
    # pascal's triangle has the answer
    pascals_triangle = PascalsTriangle()
    return max(pascals_triangle.get_layer(40))