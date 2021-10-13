# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:40:37 2021

@author: db_wi
"""

# the solution to this is somewhere in https://en.wikipedia.org/wiki/Pell%27s_equation
def euler066():
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
        iterator = root_frac + whole_frac
        if iterator >= 1:
            a_val = iterator.n // iterator.d
            iterator.n %= iterator.d
            whole_frac -= a_val
        # undo the automatic simplification if required
        w = whole_frac.n
        d = whole_frac.d
        if d != coeff_frac.d:
            w *= coeff_frac.d//d
        return (a_val,(coeff_frac,root,w))

    def get_continued_fraction(n):
        #print("BEGIN: %s" % str(n))
        regs = (nearest_root(n),(Fraction(1),n,-nearest_root(n)))
        res = [regs]
        #print(res)
        #print("%s %i %i" % regs[1])
        #input()       
        regs = get_next_in_continued_fraction(*regs[1])
        res.append(regs)
        #print(res)
        #print("%s %i %i" % regs[1])
        #input()       
        while regs[1][0] != 1:
            regs = get_next_in_continued_fraction(*regs[1])
            res.append(regs)
            #print(res)
            #print("%s %i %i" % regs[1])
            #input()
        #print("RESULT: %s" % res)
        return res 
    def minimal(d):
        try:
            e_n = 0
            r = None
            for e_n in d:
                r = e_n[1][0]
                if r.n*r.n - d*r.d*r.d == 1:
                    print("%i**2 - %i(%i**2) = 1" % (r.n,d,r.d))
                    return r.n
                e_n += 1
        except KeyboardInterrupt as e:
            if r:
                print("Interrupted at %i**2 - %i(%i**2)"% (r.n,d,r.d))
            else:
                print("Interrupted in minimal before processing took place.")
            raise e
    largest = 0
    get_continued_fraction(23)
    r = -1
    D=7
    r = get_continued_fraction(D)
    for i in range(len(r)):
        a = Fraction(r[-i-1][0])
        for j in r[-i-2:0:-1]:
            a.inverse()
            a += Fraction(1,j[0])
        a += r[0][0]
    
    a = minimal(D)
    if a > largest:
        largest = a
        r = D
    if not r == 5:
        return -1
    
    for D in range(8,1001):
        if int(sqrt(D))**2 == D:
            continue
        a = minimal(D)
        if a > largest:
            largest = a
            r = D
    return r