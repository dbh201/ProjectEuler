# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:24:47 2021

@author: db_wi
"""

def euler060():
    global PRIME_DB
    prime_concats = [None,[],[],[],[],[]]
    i = 1
    good = False
    def test_prime_for_concat(cs,p):
        if not cs:
            print(False)
            return False
        ret = False
        #for s in cs:
        for c in cs:
            ret = True
            t = int( str(c) + str(p) )
            if not PRIME_DB.check_prime(t):
                ret = False
                break
            t = int( str(p) + str(c) )
            if not PRIME_DB.check_prime(t):
                ret = False
                break
        if ret:
            return True
        return False
    while not good:
        p = PRIME_DB.get_nth(i)
        i += 1

        for p in PRIME_DB.db:
            prime_concats[1].append([p])
            for concat_len in range(4,0,-1):
                if not prime_concats[concat_len]:
                    continue
                for concat_set in range(len(prime_concats[concat_len])):
                    if test_prime_for_concat(prime_concats[concat_len][concat_set],p):
                        prime_concats[concat_len+1].append(prime_concats[concat_len][concat_set] + [p])
            if len(prime_concats[5]) > 0:
                return min([sum(x) for x in prime_concats[5]])