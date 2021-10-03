# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 13:11:12 2021

@author: db_wi
"""

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
                break
        for j in range(5):
            yield ops[j](symbols)
            #print(symbols)
            i += 1
    return

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