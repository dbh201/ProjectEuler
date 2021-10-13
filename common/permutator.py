# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 13:11:12 2021

@author: db_wi
"""
# [3dg] represents this series of instructions, which create 5 permutations:
# 0123 [swr] 01>32
# 0132 [ror] 0>213
# 0213 [swr] 02>31
# 0231 [rol] 0>312
# 0312 [swr] 03>21          (rightside 3 digits are now permuted through)

# to permute a 4 digit number:
# 0123 (the first permutation is the original ordered list)
# 0123 [3dg] 0>321

# 6 permutations so far
# 0321 [r3i] 0>123 -> 1023  (reset last 3 digits; swap left digit with one whose value is closest, yet still higher)
# 1023 [3dg] 1>320          

# 12 total permutations so far
# 1320 [r3i] 1>023 -> 2013
# 2013 [3dg] 2>310

# 18 total permutations so far
# 2310 [r3i] 2>013 -> 3012
# 3012 [3dg] 3210

# 24 permutations total for 4 digits; the last permutation is the complete reverse of the original ordered list
# of symbols

#[4dg] -> 23 permutations, consisting of all of the above instructions
# 01234 [4dg] 0>4321
# 04321 [r4i] 0>1234 -> 10234

# 24 permutations so far, including original number
# 10234 [4dg] 1>4320
# 14320 [r4i] 

# the pattern becomes obvious now: since there are 5 digits, and each digit must have a "turn" being
# the leftmost one, the amount of permutations in an x digit number is x!
# 
# in addition - to create a specific permutation, we can use the above instructions to iterate
# to it, with the xdg/rxi instructions being highly efficient shortcuts
#
# The list MUST begin in its lexicographic ascending order!
#
#swr = swap last two
#ror = rotate last three

#xdg = represents the series of instructions required to fully permute an x digit list
# [xdg] is equivalent to iterating through (x! - 1) permutations
# [xdg] is unused, but interesting to note

#rxi = reverse rightmost x digits and increment the digit 
# in the position left-adjacent to those reversed digits
# [rxi] creates the next permutation after an [xdg] instruction
# [rxi] is equivalent to iterating through x! permutations
# These functions do not make copies! They return the original list.
def ror(a,x=3):
    t = a[-1]
    for i in range(-1,-x,-1):
        a[i] = a[i-1]
    a[-x] = t
    return a

def rol(a,x=3):
    t = a[-x]
    for i in range(-x+1,0):
        a[i-1] = a[i]
    a[-1] = t
    return a

def rxi(b,x):
    if x < 3:
        raise Exception("rxi only works with x values 3 or above")
    if x >= len(b):
        print("rxi rolled over")
        return b
    leftmost = len(b)-x-1
    c = max(b[leftmost:])
    ci = b.index(c)
    for i in range(leftmost+1,len(b)):
        if b[i] < c and b[i] > b[leftmost]:
            c = b[i]
            ci = i
    if b[ci] == b[leftmost]:
        return rxi(b,x+1)
    b[ci] = b[leftmost]
    b[leftmost] = c
    return b
              
def xdg(a,x):
    if x < 3:
        raise Exception("xdg only makes sense with x values 3 or above")
    half_x = x // 2
    j = -1
    for i in range(-x,-x+half_x):
        t = a[i]
        a[i] = a[j]
        a[j] = t
        j -= 1
    return a

def swr(a):
    if a[-2] == a[-1]:
        return None
    t = a[-2]
    a[-2] = a[-1]
    a[-1] = t
    return a

def permute_iter(s):
    symbols = sorted(s)
    yield symbols
    if len(symbols) == 1:
        return
    if len(symbols) == 2:
        symbols.reverse()
        yield symbols
        return
    i = 1
    ops = [swr,ror,swr,rol,swr]
    
    facs = [ 1,1,2 ]
    while len(facs) < len(symbols)+1:
        facs.append(len(facs)*facs[-1])
    while i < facs[len(s)]:
        lastsymbols = list(symbols)
        for f in range(len(facs)-1,2,-1):
            if i % facs[f] == 0:
                #print("{: 8}-{: 8}({: 3}): {}".format(i,facs[f],f,symbols))
                xdg(symbols,f)
                #print("{: 8}-{: 8}({: 3}): {}".format(i,facs[f],f,symbols))
                rxi(symbols,f)
                #print("{: 8}-{: 8}({: 3}): {}".format(i,facs[f],f,symbols))
                #print(symbols)
                if not symbols == lastsymbols:
                    yield symbols
                i += 1
        for j in range(5):
            ops[j](symbols)
            yield symbols
            i += 1

# for the permute function, the 0th order is permutation 1, or the original ordered list
def permute(order,symbols):
    rev = False # TODO: make a reverse permuter
    #print("WARNING: This has a bug in it. YMMV.")
    facs = [1,1,2]
    while len(facs) < len(symbols)+1:
        facs.append(len(facs)*facs[-1])
        
    o = order
    s = list(symbols)
    if o >= facs[len(s)]:
        print("WARNING: order value is too large; permutations will wrap around")
        print(facs)
        print(order)
        print(symbols)
    
    for f in range(len(facs)-1,2,-1):
        while facs[f] <= o:
            s = rxi(s,f)
            #print("{: 8}-{: 8}({: 3}): {}".format(o,facs[f],f,s))
            o -= facs[f]
    
    #FIXME: This is disgusting, I know. 
    last_five_operations = [swr,ror,swr,rol,swr]
    last_op = o
    op = 0
    while op < last_op:
        s = last_five_operations[op](s)
        #print("{: 8}-{: 8}({: 3}): {}".format(o,facs[f],f,s))
        op += 1
        o -= 1
    return s