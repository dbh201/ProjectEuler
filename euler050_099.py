# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:52:05 2021

@author: db_wi
"""
from euler_common import test_palindrome,\
get_nth_triangle_number,get_nth_square_number,get_nth_pentagon_number,\
get_nth_hexagonal_number,get_nth_heptagonal_number,get_nth_octagonal_number,\
permute_iter,Fraction

from math import sqrt
# import cProfile
# import pstats
# with cProfile.Profile() as pr:
#       >do complicated stuff<
# stats = pstats.Stats(pr)
# stats.sort_stats(pstats.SortKey.TIME)
# stats.print_stats()
# stats.dump_stats(filename="this.prof")

# ---CMDLINE---
# pip install snakeviz
# snakeviz ./this.prof
# -------------

def euler050():
    plist = generate_primes(1000000,True)

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
    c = 0
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
def get_poker_hands(s):
    global vals
            
    r = [ (vals[x[0]],x[1]) for x in s.split(" ") ]
    if len(r) != 10:
        return None
    return (tuple(sorted(r[:5])),tuple(sorted(r[5:])))

def get_poker_hand_value(hand):
    global vals
    global hand_names
    
    def get_same_values(hand):
        r = []
        c1 = 0
        while c1 < len(hand):
            c = [hand[c1]]
            finished = True
            for c2 in range(c1+1,len(hand)):
                if hand[c1][0] == hand[c2][0]:
                    c.append(hand[c2])
                else:
                    c1 = c2 - 1
                    finished = False
                    break
            if len(c) > 1:
                r.append(c)
            if finished:
                return r
            c1 += 1
        return r
    
    def is_flush(v):
        for i in range(1,len(v)):
            if v[i][1] != v[i-1][1]:
                return False
        return True
    
    def is_straight(v):
        for i in range(1,len(v)):
            if v[i][0] != v[i-1][0] + 1:
                return False
        return True
    
    pairs = get_same_values(hand)
    isf = is_flush(hand)
    iss = is_straight(hand)
    
    royal_flush = (9,)
    straight_flush = (8,)
    four_of_a_kind = (7,)
    full_house = (6,)
    flush = (5,)
    straight = (4,)
    three_of_a_kind = (3,)
    two_pairs = (2,)
    one_pair = (1,)
    high_card = (0,hand[-1][0])
    
    if isf:
        if iss:
            if hand[-1][0] == 14:
                return royal_flush + (hand[-1][0],)
            return straight_flush + (hand[-1][0],)
        return flush + (hand[-1][0],)
    elif iss:
        return straight + (hand[-1][0],)
    elif pairs:
        if len(pairs) == 1:
            if len(pairs[0]) == 2:
                return one_pair + (pairs[0][-1][0],)
            if len(pairs[0]) == 3:
                return three_of_a_kind + (pairs[0][-1][0],)
            return four_of_a_kind + (pairs[0][-1][0],)
            
        
        if len(pairs[0]) == 3:
            return full_house + (pairs[0][-1][0],pairs[1][-1][0])
        if len(pairs[1]) == 3:
            return full_house + (pairs[1][-1][0],pairs[0][-1][0])
        else:
            return two_pairs + tuple(sorted( (p[-1][0] for p in pairs), reverse=True))
    return high_card

    # This isn't working?
    # if we have pairs, we cannot have a straight or flush
    if pairs:
        if len(pairs) == 1:
            if len(pairs[0]) == 2:
                return one_pair + (pairs[0][-1][0],)
            if len(pairs[0]) == 3:
                return three_of_a_kind + (pairs[0][-1][0],)
            return four_of_a_kind + (pairs[0][-1][0],)
            
        
        if len(pairs[0]) == 3:
            return full_house + (pairs[0][-1][0],pairs[1][-1][0])
        if len(pairs[1]) == 3:
            return full_house + (pairs[1][-1][0],pairs[0][-1][0])
        else:
            return two_pairs + tuple(sorted((p[-1][0] for p in pairs),reverse=True))
    elif isf:
        if iss:
            if hand[-1][0] == 14:
                return royal_flush + (hand[-1][0],)
            return straight_flush + (hand[-1][0],)
        return flush + (hand[-1][0],)
    elif iss:
        return straight + (hand[-1][0],)
    return high_card
    
def euler054():
    global vals
    vals = dict()
    for v in range(2,10):
        vals[str(v)] = v
    vals["T"] = 10
    vals["J"] = 11
    vals["Q"] = 12
    vals["K"] = 13
    vals["A"] = 14
    vals["C"] = "clubs"
    vals["D"] = "diamonds"
    vals["H"] = "hearts"
    vals["S"] = "spades"
    global hand_names
    hand_names = [
        "high card",
        "one pair",
        "two pairs",
        "three of a kind",
        "straight",
        "flush",
        "full house",
        "four of a kind",
        "straight flush",
        "royal flush"
        ]

    def player_1_wins(p1,p2):
        p1v = get_poker_hand_value(p1)
        p2v = get_poker_hand_value(p2)
        #print(hand_names[p1v[0]],"vs",hand_names[p2v[0]])
        #print(p1v,"vs",p2v)
        for i in range(len(p1v)):
            if p1v[i] > p2v[i]:
                #print("WIN BY BETTER HAND")
                return True
            elif p1v[i] < p2v[i]:
                #print("LOSS BY BETTER HAND")
                return False
            
        # the bug was here and only affected *one* hand in the 1000-hand set
        # the range was not reversed! it was comparing the size of the lowest
        # cards rather than the highest
        for i in reversed(range(len(p1))):
            if p1[i][0] > p2[i][0]:
                #print("WIN BY HIGH CARD")
                #print(p1[i],p2[i])
                return True
            elif p1[i][0] < p2[i][0]:
                #print("LOSS BY HIGH CARD")
                #print(p1[i],p2[i])
                return False
        raise ValueError("Hand values were completely identical\n%s\n%s" % (p1v,p2v))
    testhands = [
        ("5H 5C 6S 7S KD 2C 3S 8S 8D TD",False),
        ("5D 8C 9S JS AC 2C 5C 7D 8S QH",True),
        ("2D 9C AS AH AC 3D 6D 7D TD QD",False),
        ("4D 6S 9H QH QC 3D 6D 7H QD QS",True),
        ("2H 2D 4C 4D 4S 3C 3D 3S 9S 9D",True),
        ]
    for h in testhands:
        a,b = get_poker_hands(h[0])
        #print(a,"VERSUS",b)
        if player_1_wins(a,b) != h[1]:
            print("Calculation error:")
            return None
        
    with open("p054_poker.txt","r") as file:
        wins = 0
        ln = 0
        #stolen from some other nerd.... I got annoyed by a bug
        #winning_set = {2, 3, 6, 7, 10, 12, 13, 18, 20, 22, 27, 29, 30, 31, 32, 33, 35, 38, 40, 43, 44, 48, 50, 53, 57, 61, 65, 66, 67, 69, 71, 72, 76, 79, 80, 83, 85, 86, 87, 88, 91, 96, 101, 106, 110, 112, 113, 121, 122, 123, 127, 128, 130, 135, 136, 138, 140, 145, 147, 148, 150, 158, 161, 164, 167, 168, 172, 174, 175, 176, 177, 183, 189, 190, 191, 197, 199, 201, 204, 205, 212, 214, 219, 223, 230, 233, 235, 236, 237, 241, 242, 244, 247, 248, 250, 252, 255, 265, 267, 271, 272, 274, 279, 280, 281, 286, 287, 289, 290, 291, 293, 297, 305, 308, 310, 312, 315, 319, 321, 322, 323, 324, 327, 330, 333, 336, 339, 345, 348, 349, 354, 358, 360, 361, 365, 367, 368, 369, 375, 378, 381, 382, 384, 394, 398, 402, 404, 411, 412, 413, 415, 419, 423, 424, 426, 432, 433, 435, 437, 440, 442, 448, 449, 454, 455, 459, 460, 466, 467, 469, 470, 473, 475, 478, 480, 485, 489, 490, 492, 494, 495, 497, 498, 499, 500, 501, 504, 506, 512, 525, 526, 528, 529, 534, 538, 541, 550, 553, 556, 558, 560, 561, 563, 564, 565, 566, 568, 569, 570, 571, 576, 579, 585, 590, 591, 598, 599, 602, 603, 604, 605, 609, 611, 624, 625, 633, 634, 640, 641, 642, 646, 650, 653, 656, 658, 659, 660, 663, 664, 668, 671, 672, 676, 677, 680, 682, 683, 684, 686, 690, 691, 692, 693, 696, 697, 698, 701, 702, 703, 704, 705, 706, 707, 709, 712, 718, 719, 720, 722, 725, 726, 732, 734, 737, 743, 745, 748, 750, 754, 758, 761, 762, 764, 772, 773, 774, 775, 776, 779, 785, 786, 787, 791, 794, 797, 799, 803, 804, 808, 810, 812, 814, 815, 819, 820, 822, 827, 830, 831, 834, 835, 836, 839, 840, 841, 844, 845, 849, 855, 857, 860, 863, 868, 869, 871, 872, 876, 884, 885, 886, 887, 888, 890, 892, 897, 905, 907, 908, 913, 915, 917, 919, 921, 923, 929, 931, 932, 933, 934, 939, 940, 941, 947, 948, 950, 951, 954, 955, 958, 960, 962, 966, 972, 973, 974, 976, 978, 981, 983, 984, 987, 989, 990, 993, 999, 1000}
        for line in file.readlines():
            ln += 1
            p1, p2 = get_poker_hands(line)
            try:
                if player_1_wins(p1,p2):
                    wins += 1
                    #if ln not in winning_set:
                        #print("ERRONEOUS WIN ON LINE %i:" % ln)
                        #print(
                        #    ', '.join("{}{}".format(a[0],a[1]) for a in p1),
                        #    "vs",
                        #    ', '.join("{}{}".format(b[0],b[1]) for b in p2),
                        #    )
                        #input()
                else:
                    pass
                    #if ln in winning_set:
                        #print("ERRONEOUS LOSS ON LINE %i:" % ln)
                        #print(
                        #    ', '.join("{}{}".format(a[0],a[1]) for a in p1),
                        #    "vs",
                        #    ', '.join("{}{}".format(b[0],b[1]) for b in p2),
                        #    )
                        #input()
            except ValueError as e:
                print(e)
                print(p1)
                print(p2)
                input()

        return wins
    
def test_lychrel(n):
    for i in range(50):
        n += int(''.join(reversed(str(n))))
        if test_palindrome(str(n)):
            return False
    return True

def euler055():
    count = 0
    for i in range(1,10000):
        if test_lychrel(i):
            count += 1
    return count

def euler056():
    r = 0
    for a in range(1,101):
        for b in range(1,101):
            i = 0
            for c in str(pow(a,b)):
                i += int(c)
            if i > r:
                r = i
    return r
def get_root_2_fraction_terms(n,d):
    t = n
    n = d
    d = t
    d += n
    n += d
    return (n,d)
def euler057():
    n = 1
    d = 1
    r = 0
    for i in range(1000):
        n,d = get_root_2_fraction_terms(n,d)
        if len(str(n)) > len(str(d)):
            r += 1
    return r

def euler058():
    p = 0
    nums = 1
    prime_list = generate_primes(10000)
    n = 1
    it = 0
    done = False
    while not done:
        it += 2
        for i in range(4):
            nums += 1
            n += it
            if n > prime_list[-1]*prime_list[-1]:
                prime_list = generate_primes(n,True,prime_list)
            if check_prime(n,prime_list):
                
                p += 1
        if p / nums < 0.1:
            done = True
    print("%i primes out of %i numbers = %f\nside length iterator: %i" %(p,nums,p/nums,it))
    return it+1

def euler059():
    with open("p059_cipher.txt") as file:
        buffer = file.read().split(',')
        from numpy import bitwise_xor
        from string import ascii_lowercase
        search_terms = ["he","it","an","on","of","or","is"]
        result = None
        result_confidence = 0
        result_key = None
        last_confidence = None
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                key = ['a',b,c]
                temp = list(int(i) for i in buffer)
                for i in range(len(temp)):
                    temp[i] = bitwise_xor(int(temp[i]),ord(key[i%len(key)]))
                dec = ''.join(chr(t) for t in temp)
                dec_lower = str(dec).lower()
                confidence = 0
                for s in search_terms:
                    confidence += dec_lower.count(s)
                if confidence > result_confidence:
                    result = dec
                    result_confidence = confidence
                    result_key = key
        for a in ascii_lowercase:
            key = list(result_key)
            key[0] = a
            temp = list(int(i) for i in buffer)
            for i in range(len(temp)):
                temp[i] = bitwise_xor(int(temp[i]),ord(key[i%len(key)]))
            dec = ''.join(chr(t) for t in temp)
            dec_lower = str(dec).lower()
            confidence = 0
            for s in search_terms:
                confidence += dec_lower.count(s)
            if confidence > result_confidence:
                result = dec
                result_confidence = confidence
                result_key = key
        print(result)
        return sum(ord(c) for c in result)
                            
def euler060():
    prime_concats = [None,[],[],[],[],[]]
    prime_list = generate_primes(10000)
    i = 1
    good = False
    def test_prime_for_concat(cs,p,prime_list):
        if not cs:
            print(False)
            return False
        ret = False
        #for s in cs:
        for c in cs:
            ret = True
            t = int( str(c) + str(p) )
            if t > prime_list[-1]*prime_list[-1]:
                print("Generating primes... (%i was max)" % prime_list[-1])
                prime_list = generate_primes(len(prime_list)+10000,False,prime_list)
            if not check_prime(t,prime_list):
                ret = False
                break
            t = int( str(p) + str(c) )
            if not check_prime(t,prime_list):
                ret = False
                break
        if ret:
            return True
        return False
    while not good:
        if i >= len(prime_list):
            print("Generating primes... (%i was max)" % prime_list[-1])
            prime_list = generate_primes(len(prime_list)+10000,False,prime_list)
        p = prime_list[i]
        i += 1
        found_two = False
        found_three = False
        found_four = False
        found_five = False
        for p in prime_list:
            prime_concats[1].append([p])
            for concat_len in range(4,0,-1):
                if not prime_concats[concat_len]:
                    continue
                for concat_set in range(len(prime_concats[concat_len])):
                    #print("Testing prime %i in set %s" % (p,prime_concats[concat_len][concat_set]))
                    if test_prime_for_concat(prime_concats[concat_len][concat_set],p,prime_list):
                        #print("%i %s" % (concat_len+1,prime_concats[concat_len][concat_set] + [p]))
                        prime_concats[concat_len+1].append(prime_concats[concat_len][concat_set] + [p])
            if not found_two and len(prime_concats[2]) > 0:
                print("2",prime_concats[2])
                found_two = True
            if not found_three and len(prime_concats[3]) > 0:
                print("3",prime_concats[3])
                found_three = True
            if not found_four and len(prime_concats[4]) > 0:
                print("4",prime_concats[4])
                found_four = True
            if not found_five and len(prime_concats[5]) > 0:
                print("5",prime_concats[5])
                found_five = True
                return min([sum(x) for x in prime_concats[5]])

def solve_quadratic(a,b,c):
    determinate = sqrt((b*b) - (4*a*c))
    return ((-b + determinate)/(2*a),(-b - determinate)/(2*a))

def get_positive_solution(r):
    if r[0] > 0 and r[0] == int(r[0]):
        return int(r[0])
    if r[1] > 0 and r[1] == int(r[1]):
        return int(r[1])
    return None

def is_triangle_number(y):
    r = solve_quadratic(0.5,0.5,-y)
    return get_positive_solution(r)
    

def is_square_number(y):
    r = solve_quadratic(1,0,-y)
    return get_positive_solution(r)

def is_pentagonal_number(y):
    r = solve_quadratic(3/2,-1/2,-y)
    return get_positive_solution(r)

def is_hexagonal_number(y):
    r = solve_quadratic(2,-1,-y)
    return get_positive_solution(r)

def is_heptagonal_number(y):
    r = solve_quadratic(5/2,-3/2,-y)
    return get_positive_solution(r)

def is_octagonal_number(y):
    r = solve_quadratic(3,-2,-y)
    return get_positive_solution(r)

def euler061():
    tests = [
        is_triangle_number,
        is_square_number,
        is_pentagonal_number,
        is_hexagonal_number,
        is_heptagonal_number,
        is_octagonal_number
    ]
    def test_cascade(n,t):
        for test in t:
            r = test(n[-2]*100+n[-1])
            if r:
                print("Test:",n,n[-2]*100+n[-1],test.__name__,r)
                tn = list(t)
                tn.remove(test)
                if len(tn) == 1:
                    r = tn[0](n[-1]*100+n[0])
                    if r:
                        print("Final:",n,n[-1]*100+n[0],tn[0].__name__,r)
                        print("returning",n)
                        return n
                    return None
                for c in range(10,100):
                    r = test_cascade(n+[c],tn)
                    if r:
                        print("returning",n+[c])
                        return r
                break
        return None
    print(test_cascade([81,28],tests[:3]))
    for a in range(10,100):
        for b in range(10,100):
            r = test_cascade([a,b],tests)
            if r:
                ret = r[-1]*100+r[0]
                for i in range(len(r)-1):
                    ret += r[i]*100+r[i+1]
                return ret

def get_permutation_count(n,cubes,max_cube,max_idx):
    permutations = set()
    i = 0
    for iterator in permute_iter(str(n)):
        i += 1
        iter_int = int(''.join(iterator))
        while iter_int > max_cube:
            max_idx += 1
            max_cube = max_idx**3
            cubes.add(max_cube)
        if iter_int in cubes:
            permutations.add(iter_int)
    print(permutations,max_cube,i)
    return (len(permutations),cubes,max_cube,max_idx)

# INCOMPLETE - need better algo for permutation count
def euler062():
    cubes = set()
    cubes.add(1)
    max_cube = 1
    max_idx = 1
    done = False
    i = 2
    print(get_permutation_count(345**3,cubes,max_cube,max_idx)[0])
    return
    while not done:
        c = i**3
        permutations,cubes,max_cube,max_idx = get_permutation_count(c, cubes, max_cube, max_idx)
        if permutations == 5:
            return c
        i += 1

def euler063():
    powers = []
    done = False
    i = 1
    p = 1
    c = 0
    cip = 0
    while not done:
        s = str(i**p)
        if len(s) > p:
            if cip == 0:
                break
            p += 1
            i = 1
            c += cip
            cip = 0
        elif len(s) == p:
            cip += 1
            i += 1
        else:
            i += 1
    return c

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
            if r % 10 == 0:
                print(r,i)
            r += 1
    return r

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
            print("Final depth (%i): %s" % (maxdepth,r))
            return Fraction(r)
        r = build_e(maxdepth,depth+1).inverse()
        r2 = get_e_cont(depth)
        print("Depth %i: %i + %s" % (depth,r2,r))
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
    print(num_recurse(10))
    return sum([int(i) for i in str(num_recurse(100))])
        
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
            done = False
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
    print("D: %i" % D)
    r = get_continued_fraction(D)
    for i in range(len(r)):
        a = Fraction(r[-i-1][0])
        for j in r[-i-2:0:-1]:
            a.inverse()
            a += Fraction(1,j[0])
        a += r[0][0]
        print("Depth %i: %s" % (i,a))
    return   
    
    a = minimal(D)
    if a > largest:
        largest = a
        r = D
    if r == 5:
        print("Test case passed")
    else:
        print("Test case failed")
        return
    
    for D in range(8,1001):
        if int(sqrt(D))**2 == D:
            continue
        a = minimal(D)
        if a > largest:
            largest = a
            r = D
    print(timeouts)
    return r
def euler067():
    pass