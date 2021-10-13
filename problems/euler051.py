# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:03:57 2021

@author: db_wi
"""

def euler051():
    pset = set()
    mask = 0
    for p in PRIME_DB.db:
        ps = str(p)
        for m in range(1,2**len(ps)-1):
            s = list(ps)
            mask = ("{:0" + str(len(s)) + "b}").format(m)
            for i in range(len(mask)):
                if mask[i] == "1":
                    s[i] = "*"
            pstr = ''.join(s)
            pvals = []
            if not pstr in pset:
                for val in range(1,10):
                    ptest = pstr.replace('*', str(val))
                    if PRIME_DB.check_prime(int(ptest)):
                        pvals.append(ptest)
                if len(pvals) == 8:
                    return int(pvals[0])
                pset.add(pstr)