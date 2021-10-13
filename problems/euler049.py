# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:46:22 2021

@author: db_wi
"""

def euler049():
    plist = PRIME_DB.get_prime_list(max_prime=10000)
    start_prime = 0
    while plist[start_prime] < 1000:
        start_prime += 1
    pset = set(plist[start_prime:])
    # remove test case
    pset.remove(1487) 
    pset.remove(4817) 
    pset.remove(8147) 
    for prime in pset:
        for interval in range(2,3331,2):
            if prime + 2*interval >= 10000:
                break
            if prime + interval in pset and prime + 2*interval in pset:
                p1 = str(prime)
                p2 = str(prime + interval)
                p3 = str(prime + (2*interval))
                passed = True
                for i in range(10):
                    c = str(i)
                    p1c = p1.count(c)
                    if p1c != p2.count(c) or p1c != p3.count(c):
                        passed = False
                        break
                if passed:
                    return int(str(prime) + str(prime+interval) + str(prime+ (2*interval)))