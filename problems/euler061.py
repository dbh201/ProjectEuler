# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:24:49 2021

@author: db_wi
"""

def euler061():
    tria = TriangleNumberSequence()
    squa = SquareNumberSequence()
    pent = PentagonalNumberSequence()
    hexa = HexagonalNumberSequence()
    hept = HeptagonalNumberSequence()
    octa = OctagonalNumberSequence()
    tests = [
        tria,
        squa,
        pent,
        hexa,
        hept,
        octa
    ]
    def test_cascade(n,t):
        for test in t:
            r = test.get_inv(n[-2]*100+n[-1])
            if r:
                tn = list(t)
                tn.remove(test)
                if len(tn) == 1:
                    r = tn[0].get_inv(n[-1]*100+n[0])
                    if r:
                        return n
                    return None
                for c in range(10,100):
                    r = test_cascade(n+[c],tn)
                    if r:
                        return r
                break
        return None
    for a in range(10,100):
        for b in range(10,100):
            r = test_cascade([a,b],tests)
            if r:
                ret = r[-1]*100+r[0]
                for i in range(len(r)-1):
                    ret += r[i]*100+r[i+1]
                return ret
    return None
    