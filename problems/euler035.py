# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:22:41 2021

@author: db_wi
"""

def euler035():
    circular_primes = set()
    plist = PRIME_DB.get_prime_list(max_prime=1000000)
    def ror(i):
        s = str(i)
        return s[1:] + s[0]
    
    for p in plist:
        if p in circular_primes:
            continue
        orig_p = str(p)
        p_set = set()
        p_set.add(p)
        next_p = ror(p)
        is_circular = True
        while next_p != orig_p:
            this_p = int(next_p)
            if not PRIME_DB.check_prime(this_p):
                is_circular = False
                break
            p_set.add(this_p)
            next_p = ror(next_p)
        
        if is_circular:
            circular_primes.update(p_set)
    return len(circular_primes)