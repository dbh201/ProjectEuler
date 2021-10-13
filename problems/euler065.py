# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:37:08 2021

@author: db_wi
"""

def euler065():
    def get_e_cont(n):
        if n == 0:
            return 2
        if n%3 != 2:
            return 1
        return 2*((n//3)+1)
    # this is categorically too slow
    def build_e(maxdepth,depth=0):
        if depth == maxdepth:
            r = get_e_cont(depth)
            return Fraction(r)
        r = build_e(maxdepth,depth+1).inverse()
        r2 = get_e_cont(depth)
        r += r2
        #specifically here - the num/den get huge
        if depth%2 == 0:
            r.simplify()
        return r
    
    # f = build_e(99)
    # here's a cheat: numerator for convergent number k
    # n_k = get_e_cont(k)*n_(k-1) + n_(k-2)
    # simple as. here's the function
    nums = [2,3,8]
    def num_recurse(k):
        for i in range(len(nums),k):
            nums.append(get_e_cont(i)*nums[-1]+nums[-2])
        return nums[k-1]
    return sum([int(i) for i in str(num_recurse(100))])