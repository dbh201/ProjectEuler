# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:24:43 2021

@author: db_wi
"""

def euler037():
    tpr = set()
    i = 4
    while len(tpr) < 11:
        p = PRIME_DB.db[i]
        s = str(p)
        i += 1
        if not PRIME_DB.check_prime(int(s[0])) or not PRIME_DB.check_prime(int(s[-1])):
            continue
        #print(s + " passed initial.")

        failed = False
        
        sltr = s[1:]
        while len(sltr) > 1:
            if not PRIME_DB.check_prime(int(sltr)):
                failed = True
                break
            sltr = sltr[1:]
        if failed:
            continue
        #print(s + " passed ltr.")
        
        srtl = s[:-1]
        while len(srtl) > 1:
            if not PRIME_DB.check_prime(int(srtl)):
                failed = True
                break
            srtl = srtl[:-1]
        if failed:
            continue
        #print(s + " passed rtl.")
        tpr.add(p)
            
    #print(tpr)
    return sum(tpr)
        