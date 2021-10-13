# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:24:02 2021

@author: db_wi
"""

def euler036():
    return sum( [ i for i in range(1,1000000,2) if test_palindrome(str(i)) and test_palindrome(str(bin(i))[2:]) ] )