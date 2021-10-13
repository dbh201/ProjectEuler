# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:58:15 2021

@author: db_wi
"""

def euler026():
    # what I know so far:
    # - All prime numbers make repeating decimals, except for the ones coprime to our number system (2, and 5).
    # - floats, doubles, and long-doubles likely have insufficient accuracy for our purposes. We need 100% accurate
    #   numbers of indeterminate length. Speedy calculations are secondary.
    #
    #--We can get an infinite list of digits with the following algorithm:
    # -> begin by setting our "remainder" to a power of 10 greater than the prime being tested
    # --> this power of 10 will remove leading zeroes, which are not useful to the calculation, from the result
    # -> (remainder) // prime = resultant digit
    # -> ((remainder) % prime)*10 = remainder to be used for the next digit
    # This can be repeated infinitely.
    #-----
    def get_next_number(remainder, prime):
        return remainder // prime
    def get_next_remainder(remainder, prime):
        return (remainder % prime) * 10

    # This is actually unnecessary, but cool for a conceptual repetition test - works with any data :)
    def get_longest_cycle(l,minimum=2):
        r = []
        for i in range(len(l)):
            for rm in range(minimum,(len(l)//2)+1-i):
                #print("Testing for sequence of size %i at location %i" % (rm,i))
                found = True
                for k in range(0,rm):
                    if l[i+k] != l[i+rm+k]:
                        #print("l[%i] %i != l[%i] %i" % (i,l[i],i+k,l[i+k]))
                        found = False
                if found:
                    #print("Found sequence.")
                    d = l[i]
                    good = False
                    for d2 in l[i+rm:]:
                        if d != d2:
                            good = True
                    if good:
                        #print("Sequence good!")
                        r.append(rm)
                    else:
                        return 1
                    
        if len(r) > 0: return r[-1]
        return None
    #--FROM WIKIPEDIA:
    # The length of the repetend (period of the repeating decimal segment) of 1/p
    # is equal to the order of 10 modulo p.
    #-----
    #
    # that sounds, to a non-mathematician, like larger values of p produce longer repetends
    # so I'll reverse the prime list.
    # 
    prime_list = [3] + PRIME_DB.get_prime_list(max_prime=1000)[3:]
    cm = 0
    cp = 0
    for p in reversed(prime_list):
        digit_list = []
        r = 1
        while r < p:
            r *= 10
        r //= 10
        c = None
        while True:
            for v in range(100):
                digit_list.append(r//p)
                r = (r % p) * 10
                if r == 10:
                    c = len(digit_list)
                    break
            if c:
                break
            # This whole thing was unnecessary - just have to check if the remainder is 1
            # If the remainder is 1, then we can assume the whole process will repeat itself.
            # recalculation galore here - fix it!
            # c = get_longest_cycle(digit_list,m)
            #if c:
            #   break
            #else:
            #    if not m == 2:
            #        m += 50
            #    else:
            #        m = 50
                #print("%i: no sequences yet (tested to length %i)" % (p,m))
        #print("%i: %i" % (p,c))
        if c > cm:
            cm = c
            cp = p
    #print("denominator %i has cycle length %i" % (cp,cm))
    return cp