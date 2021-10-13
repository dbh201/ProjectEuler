# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:13:00 2021

@author: db_wi
"""

def test_pandigital(n,digits=9):
    s = str(n)
    if len(s) != digits:
        return False
    for i in range(1,digits+1):
        if s.count(str(i)) != 1:
            return False
    return True

def test_palindrome(s):
    sl = s[:len(s)//2]
    if len(s)%2:
        sr = s[:(len(s)//2):-1]
    else:
        sr = s[:(len(s)//2)-1:-1]
    return sl == sr

def test_lychrel(n):
    for i in range(50):
        n += int(''.join(reversed(str(n))))
        if test_palindrome(str(n)):
            return False
    return True