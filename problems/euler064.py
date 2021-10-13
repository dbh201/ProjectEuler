# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:36:36 2021

@author: db_wi
"""

#INCOMPLETE - need information on continued fractions
# a0 + 1/ (a1 + 1/  .. etc)
# ax + nx/dx 
# PROCESS:
    # invert fraction
    # multiply fraction by conjugate
    # simplify result
    # resolve expression into a mixed fraction
    # -> repeat if necessary

def euler064():
    nroots = dict()
    def nearest_root(n):
        if n not in nroots:
            nroots[n] = int(sqrt(n))
        return nroots[n]
    
    def get_next_in_continued_fraction(coeff,root,whole):
        #invert and multiply by conjugate
        # AKA fraction = (prev_denominator * (sqrt(root)-whole))/(prev_coeff*(root - whole**2))
        # fraction must be < 1; integer portion is new a_n
        coeff_frac = coeff.inverse()
        coeff_frac *= Fraction(1,root - whole**2)
        #print("Coeff: %s (%s)" % (coeff_frac,coeff))
        # fraction = coeff_frac * sqrt(root) - coeff_frac * whole; whole being < 0
        root_frac = Fraction(coeff_frac)*(nearest_root(root))
        #print("Root: %s (%i)" % (root_frac,root))
        whole_frac = Fraction(coeff_frac)*(-whole)
        a_val = 0
        while (root_frac + whole_frac) >= 1:
            #print(root_frac + whole_frac)
            whole_frac -= 1
            a_val += 1
        # undo the automatic simplification if required
        w = whole_frac.n
        d = whole_frac.d
        if d != coeff_frac.d:
            w *= coeff_frac.d//d
        return (a_val,(coeff_frac,root,w))
    def get_continued_fraction(n):
        #print("BEGIN: %s" % str(n))
        regs = (nearest_root(n),(Fraction(1),n,-nearest_root(n)))
        res = [regs[0]]
        #print(res)
        #print("%s %i %i" % regs[1])
        #input()       
        regs = get_next_in_continued_fraction(*regs[1])
        res.append(regs[0])
        #print(res)
        #print("%s %i %i" % regs[1])
        #input()       
        while regs[1][0] != 1:
            regs = get_next_in_continued_fraction(*regs[1])
            res.append(regs[0])
            #print(res)
            #print("%s %i %i" % regs[1])
            #input()
        #print("RESULT: %s" % res)
        return res

    r=0
    for i in range(2,10001):
        nr = nearest_root(i)
        if nr**2 == i:
            continue
        a = get_continued_fraction(i)
        if (len(a)-1)%2 == 1:
            r += 1
    return r