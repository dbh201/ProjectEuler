# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:55:58 2021

@author: db_wi
"""
PRIMES = set([2,3,5])
PRIMES_LIST = [2,3,5]
# print("Making some primes...")
# for i in range(7,1000000,2):
#     prime = True
#     for p in PRIMES_LIST:
#         if p*p > i:
#             break
#         if i % p == 0:
#             prime = False
#             break
#     if(prime):
#         PRIMES.add(i)
#         PRIMES_LIST.append(i)


    






def test_palindrome(s):
    sl = s[:len(s)//2]
    if len(s)%2:
        sr = s[:(len(s)//2):-1]
    else:
        sr = s[:(len(s)//2)-1:-1]
    return sl == sr

gd_cache = dict()
def get_divisors(n):
    if n in gd_cache:
        return gd_cache[n]
    d = [1]
    d2 = [n]
    j = 2
    while j*j < n:
        if not (n%j):
            if (n//j) in gd_cache:
                gd_cache[n] = list(gd_cache[n//j])
                for p in gd_cache[n//j]:
                    p2 = p*(j)
                    if not p2 in gd_cache[n]:
                        gd_cache[n].append(p2)
                gd_cache[n].sort()
                return gd_cache[n]
            d.append(j)
            d2.append(n//j)
        j += 1
    if j*j == n:
        d.append(j)
    d2.reverse()
    d.extend(d2)
    gd_cache[n] = d
    return d

def generate_pascals_triangle_layer(buffer):
    buffer.append([0 for x in range(len(buffer[-1])+1)])
    buffer[-1][0]=1
    buffer[-1][-1]=1
    for i in range(1,len(buffer[-1])-1):
        buffer[-1][i] = buffer[-2][i]+buffer[-2][i-1]
    return buffer

def get_proper_divisors_sum(n):
    d = get_divisors(n)[:-1]
    return sum(d)



def test_pandigital(n,digits=9):
    s = str(n)
    if len(s) != digits:
        return False
    for i in range(1,digits+1):
        if s.count(str(i)) != 1:
            return False
    return True
