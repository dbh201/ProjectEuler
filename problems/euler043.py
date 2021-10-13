# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:29:31 2021

@author: db_wi
"""

def euler043():
    r = 0
    a = [x for x in range(10)]
    
    def has_properties(b):
        divisors = [7,11,13,17]
        passed = True
        if b[3] % 2 > 0:
            return False
        if (b[2]+b[3]+b[4]) % 3 > 0:
            return False
        if b[5] % 5 > 0:
            return False
        substr = ''.join([str(c) for c in b[4:]])
        for tester in range(4):
            sub = int(substr[tester:tester+3])
            if sub % divisors[tester] > 0:
                passed = False
                break
        return passed
    if not has_properties(list([int(x) for x in "1406357289"])):
        print("ERROR IN TESTING FUNCTION")
        return 
    for l in permute_iter(a):
        if has_properties(l):
            r += int(''.join([str(c) for c in l]))
    return r