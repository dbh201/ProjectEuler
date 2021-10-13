# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:20:24 2021

@author: db_wi
"""

def euler033():
    num = set()
    den = set()
    for a in range(10):
        for b in range(10):
            for c in range(10):
                try:
                    frac = (a*10 + b) / (b*10 + c)
                    if frac >= 1 or frac <= 0:
                        continue
                    test = a/c
                except ZeroDivisionError: # YOLO EAFP! GO PYTHON!
                    continue
                # no need to compensate for rounding error == GO PYTHON!
                #if frac >= test - 0.00000001 and frac < test + 0.00000001:
                if frac == test:
                    #print(str(a*10 + b),"/",str(b*10 + c)," == ",str(a),"/",str(c))
                    num.add(a*10 + b)
                    den.add(b*10 + c)
    n = 1
    for i in num:
        n *= i
    d = 1
    for i in den:
        d *= i
    for i in PRIME_DB.db:
        if i > n or i > d:
            break
        while (n % i == 0 and d % i == 0):
            n //= i
            d //= i
    return d