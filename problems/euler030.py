# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:19:21 2021

@author: db_wi
"""

def euler030():
    def sum_pow(a,p=5):
        s = str(a)
        r = 0
        #print("%i -> "%a,end="")
        for c in s:
            pc = int(c)**p
            #print("%i " %pc,end="")
            r += pc
       #print(" = %i"%r)
        return r
    #print(1634 == sum_pow(1634,4))
    
    num = 2
    total = 0

    # this wasn't a good way. on the forum there's a better way:
    # just check the maximum possible sum of quintics:
    # 1* 9**5 = 59049, which is greater than 9 (max 1-digit number)
    # 6* 9**5 = 354294, which is smaller than 999999 (max 6-digit number)
    # 7* 9**5 = 413343, which is smaller than 9999999
    # As the numbers go up and up, the chances get smaller and smaller of
    # having a number whose value is below the sum of quintics of its digits.
    # once its value is guaranteed to be above the value of its quintics, then
    # we can stop.

    # we know for certain this will happen, as the sum-of-quintics
    # seems to be approximately logarithmic.
    
    #while times_not_found < 1000000:
    while num < (6* (9**5)):
        spn = sum_pow(num)
        if num == spn:
            total += num
        #else:
            #times_not_found += 1
        num += 1
    return total