# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:52:05 2021

@author: db_wi
"""

def euler050():
    plist = generate_primes(1000000,True)
    s = 0
    l = len(plist)
    p = sum(plist)
    while p > 1000000:
        p -= plist[l-1]
        l -= 1
    while l > 0:
        orig = p
        print(orig)
        for i in range(len(plist)-l):
            test = p - plist[i] + plist[l+i]
            if test > 1000000:
                break
            p = test
        if check_prime(p,plist):
            return p
        p = orig - plist[l-1]
        l -= 1
        
def euler051():
    plist = generate_primes(1000000,True)
    pset = set()
    mask = 0
    for p in plist:
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
                print("---" + pstr + "---")
                for val in range(1,10):
                    ptest = pstr.replace('*', str(val))
                    if check_prime(int(ptest),plist):
                        pvals.append(ptest)
                    else:
                        print()
                if len(pvals) == 8:
                    return pvals[0]
                pset.add(pstr)

def euler052():
    def counts(n):
        f = str(n)
        l = [ 0 for x in range(10) ]
        for i in f:
            l[int(i)] += 1
        return ''.join([str(i) for i in l])
    x = 10
    s = 10
    f = 17
    while True:
        cnts = counts(x)
        found = True
        for i in range(2,7):
            if not counts(x*i) == cnts:
                found = False
                break
        if not found:
            x += 1
            if x == f:
                f = (f-1)*10 + 7
                s *= 10
                x = s
        else:
            for i in range(1,7):
                print(x*i,counts(x*i))
            return x

def euler053():
    vs = 1
    vf = 1
    d = 1
    c = 0
    r = 1
    for n in range(1,101):
        vs = n
        rs = 1
        while vs <= 1000000 and rs < n:
            vs *= (n - rs)
            rs += 1
            vs //= rs

        vf = n
        rf = n - 1
        while vf <= 1000000 and rf > 0:
            vf *= rf
            rf -= 1
            vf //= (n-rf)
            
        if rf >= rs:
            c += (rf - rs + 1)
        
    return c

def get_poker_hand_value(s):
    hand = s.split(" ")
    vals = dict()
    for v in range(2,11):
        vals[str(v)] = v
    vals["J"] = 11
    vals["Q"] = 12
    vals["K"] = 13
    vals["A"] = 14
    def high_card(hand):
        r = hand[0]
        for card in hand[1:]:
            if vals[card[0]] > vals[r[0]]:
                r = card
        return r
    def one_pair(hand):
        pass
    def two_pair(hand):
        pass
    def three_of_a_kind(hand):
        pass
    def straight(hand):
        pass
    def full_house(hand):
        pass
    def four_of_a_kind(hand):
        pass
    def straight_flush(hand):
        pass
    def royal_flush(hand):
        pass
    hand_values = [
        high_card,
        one_pair,
        two_pairs,
        three_of_a_kind,
        straight,
        flush,
        full_house,
        four_of_a_kind,
        straight_flush,
        royal_flush,
        ]
    
def euler054():
    