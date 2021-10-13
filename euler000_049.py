# Generate a fibonacci sequence of size n *OR*
# if limit is True, then generate a fibonacci sequence
# where the maximum value is below n
from euler_common import generate_primes,generate_fibonacci_sequence
from euler_common import generate_pascals_triangle_layer,get_divisors
from euler_common import check_prime,check_prime_slow,test_palindrome
from euler_common import permute,get_proper_divisors_sum,get_nth_factorial
from euler_common import test_pandigital,permute_iter,get_nth_triangle_number
from euler_common import get_nth_hexagonal_number,get_nth_pentagon_number
def euler001():
    r = 0
    for i in range(1001):
        if not (i % 3) or not (i % 5):
            r += i
    return r

def euler002():
    a = generate_fibonacci_sequence(4000000,True)
    r = 0
    for i in a:
        if not (i%2):
            r += i
    return r

def euler003():
    lpf = 600851475143
    # This is a bit brute-force... 
    a = generate_primes( 1000000, True )
    r = -1
    for i in a:
        while not (lpf % i):
            lpf = lpf//i
            r = i
        if lpf == 1:
            break
    return r
def euler004():
    r = -1
    for a in range(999,99,-1):
        for b in range(a,99,-1):
            candidate = a*b
            if candidate < r:
                break
                    
            if test_palindrome(str(candidate)):
                r = candidate
    return r
                
def euler005():
    primes = [2,3,5,7,11,13,17,19]
    # Prime factors - we're going to reconstruct the number
    # by figuring out which prime factors we need, and how many
    pfs = [0,0,0,0,0,0,0,0]

    # scan the numbers as required by the question
    for i in range(20,1,-1):
        # check their prime factors
        for j in range(len(primes)):
            k = 0
            l = i
            while not (l%primes[j]):
                l //= primes[j]
                k +=  1
            # keep track of how many we need, at maximum
            if k > pfs[j]:
                pfs[j] = k

    # reconstruct number
    r = 1
    for i in range(len(primes)):
        r *= primes[i]**pfs[i]

    return r
            
def euler006():
    # sum of squares: n(n+1)(2n+1)/6
    # square of sums: (n(n+1)/2)**2
    return ((100*101//2)**2)-(100*101*201//6)
def euler007():
    return generate_primes(10001)[-1]
def euler008():
    s = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""
    s = s.replace('\n',"")
    s = s.replace(" ","")

    # Dumb way
    r = -1
    for i in range(len(s)-13):
        candidate = 1
        for x in s[i:i+13]:
            candidate *= int(x)
        if candidate > r:
            r = candidate

    return r


def euler009():
    for a in range(1,1001):
        for b in range(a+1,1001):
            c_sq = a**2 + b**2
            if not c_sq == (1000 - a - b)**2:
                continue
            return a*b*(1000-a-b)

def euler010():
    a = generate_primes(2000000,True)
    return sum(a)

def euler011():
    grid="""
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""
    grid = grid.strip('\n')
    print(grid)
    grid = [[int(x) for x in y.rstrip(' ').split(' ')] for y in grid.split('\n')]
    # we need to check 4 directions: vertical, horizontal,
    # ascending diagonal, and descending diagonal
    # grid coordinates are in the form grid[row][col] or grid[y][x]

    #horizontal
    r = -1
    for line in grid:
        for i in range(17):
            candidate = line[i]*line[i+1]*line[i+2]*line[i+3]
            if candidate > r:
                r = candidate
    
    #vertical
    for i in range(20):
        for j in range(17):
            candidate = grid[j][i]*grid[j+1][i]*grid[j+2][i]*grid[j+3][i]
            if candidate > r:
                r = candidate

    #ascending diagonal
    for i in range(17):
        for j in range(3,20):
            candidate = grid[j][i]*grid[j-1][i+1]*grid[j-2][i+2]*grid[j-3][i+3]
            if candidate > r:
                r = candidate
    
    #descending diagonal
    for i in range(17):
        for j in range(17):
            candidate = grid[j][i]*grid[j+1][i+1]*grid[j+2][i+2]*grid[j+3][i+3]
            if candidate > r:
                r = candidate
    return r
    
def euler012():
    # starting triangle number
    i = 10
    n = 55
    d = 0
    while d < 500:
        i += 1
        n += i
        d = len(get_divisors(n))
    return n

def euler013():
    s = '''37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690'''
    nums = [ int(i) for i in s.strip().split('\n') ]
    res = 0
    for num in nums:
        res += num
    # too easy...
    return int(str(res)[:10])
            
def euler014():
    md = 0
    mn = 0
    chains = dict()
    for m in range(1,1000000,1):
        d = 0
        chain = []
        n = m
        while n > 1:
            chain.append(n)
            if n in chains and chains[n] > 0:
                d += chains[n]
                break
            if (n%2):
                n = (n*3) + 1
            else:
                n = n//2
            d += 1
        chain.append(1)
        for c in range(len(chain)):
            if not chain[c] in chains:
                chains[chain[c]] = len(chain)-c
        if d > md:
            md = d
            mn = m
    return mn

def euler015():
    # to answer this question, we reframe it to:
    # "how many ways are there to get to this point, several layers down,
    # if each point in each layer has 1 or 2 paths leading to it?"
    # pascal's triangle has the answer
    pascals_triangle = [ [1],[1,1],[1,2,1] ]
    for i in range(38):
        pascals_triangle = generate_pascals_triangle_layer(pascals_triangle)
    print(len(pascals_triangle))
    print(max(pascals_triangle[-1]))

def euler016():
    a = str(2**1000)
    r = 0
    for i in a:
        r += int(i)
    return r

def euler017():
    ones = [
        0, # makes it easier to index
        len("one"),
        len("two"),
        len("three"),
        len("four"),
        len("five"),
        len("six"),
        len("seven"),
        len("eight"),
        len("nine"),
        ]
    teens = [
        len("ten"),
        len("eleven"),
        len("twelve"),
        len("thirteen"),
        len("fourteen"),
        len("fifteen"),
        len("sixteen"),
        len("seventeen"),
        len("eighteen"),
        len("nineteen"),
        ]
    tens = [
        0,
        len("ten"),
        len("twenty"),
        len("thirty"),
        len("forty"),
        len("fifty"),
        len("sixty"),
        len("seventy"),
        len("eighty"),
        len("ninety"),
        ]
    hundred = len("hundred")
    thousand = len("thousand")

    r = 0
    for i in range(1,1000):
        o = i % 10
        t = (i % 100)//10
        h = i//100
        if h > 0:
            r += ones[h] + hundred
            if o+t > 0:
                r += len("and")
        if t <= 1:
            if t == 1:
                r += teens[o]
            else:
                r += ones[o]
        else:
            r += tens[t] + ones[o]
            
            
    r += ones[1] + thousand
    return r

def euler018():
    s="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    layers = [[int(r) for r in l.strip().split(' ')] for l in s.split('\n')]
    best_path = [[layers[0][0]]]
    for l in range(1,len(layers)):
        best_path.append([None for x in range(len(layers[l]))])
        for c in range(len(layers[l])):
            if c == 0:
                path = c
            elif c >= len(layers[l-1]):
                path = c-1
            else:
                path = c if best_path[l-1][c] > best_path[l-1][c-1] else c-1
            best_path[l][c] = best_path[l-1][path] + layers[l][c]
        print(best_path[-1])
    return max(best_path[-1])

def euler019():
    import datetime
    r = 0
    for year in range(1901,2001):
        for month in range(12):
            d = datetime.date(year,month+1,1)
            if d.weekday() == 6:
                r += 1
    return r

def euler020():
    f = 1
    for i in range(1,101):
        f = f*i
        
    r = 0
    for i in str(f):
        r += int(i)
    return r

def euler021():
    proper_divisors = dict()
    r = 0
    for i in range(1,10000):
        if not i in proper_divisors:
            ipd = get_divisors(i)
            proper_divisors[i] = sum(ipd[:-1])
            j = proper_divisors[i]
            if j == i:
                continue
            if not j in proper_divisors:
                jpd = get_divisors(j)
                proper_divisors[j] = sum(jpd[:-1])
            if proper_divisors[j] == i:
                r += proper_divisors[i] + proper_divisors[j]
    return r
        
def euler022():
    with open("p022_names.txt") as file:
        namelist = list(map(lambda inp: inp.strip('"'),file.read().split(',')))
        
        namelist.sort()
        r = 0
        for name_idx in range(len(namelist)):
            cl = 0
            for c in namelist[name_idx]:
                cl += ord(c) - ord('A') + 1
            cl *= (name_idx+1)
            r += cl
        return r

def euler023():
        abundant = set([12,18])
        r = 171
        for i in range(19,28124):
            isd = get_proper_divisors_sum(i)
            if isd > i:
                abundant.add(i)
            add_to_result = True
            for a in abundant:
                if (i-a) in abundant:
                    add_to_result = False
                    break
            if add_to_result:
                r += i
            if not (i % 500):
                print("%i (%i) [%i]" % (i,a or -1,r))
        return r


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

#rxi = reverse rightmost x digits and increment the digit in the position left-adjacent to those reversed digits
# [rxi] creates the next permutation after an [xdg] instruction
# [rxi] is equivalent to iterating through x! permutations

def euler024():
    return permute(1000000-1,[0,1,2,3,4,5,6,7,8,9])

def euler025():
    l = [1,1]
    while len(str(l[-1])) < 1000:
        l.append(l[-2]+l[-1])
    return len(l)

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
        done = False
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
    prime_list = [3]+ generate_primes(1000,True)[3:]
    cm = 0
    cp = 0
    for p in reversed(prime_list):
        digit_list = []
        r = 1
        while r < p:
            r *= 10
        r //= 10
        c = None
        m = 2
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
    print("denominator %i has cycle length %i" % (cp,cm))
    return cp


def euler027():
    prime_list = generate_primes(10000)
    max_prime = prime_list[-1]
    max_n = 0
    retval = None
    for a in range(-999,1000):
        for b in range(-999,1000):
            n = 0
            r = n**2 + a*n + b
            if r < 2:
                continue
            while check_prime(r,prime_list):
                n += 1
                r = n**2 + a*n + b
                if r < 2:
                    break
                if r > max_prime:
                    print("Ran out of primes!")
                    prime_list = generate_primes(len(prime_list)+1000,False,prime_list)
            if n > max_n:
                print("Found a=%i,b=%i" % (a,b))
                max_n = n
                retval = a*b
    return retval

def euler028():
    WIDTH = 1001
    def ret(width):
        if not width%2:
            print("side width must be odd")
            return None
        acc = 0
        r = 1
        it = 1
        w = 2
        while w <= width:
            for i in range(4):
                it += w
                #print("%i: %i [%i]" % (r,it,w),end=" ")
                r += it
                #print("-> %i" % r)
            w += 2
        return r
    return ret(1001)

def euler029():
    terms = set()
    for a in range(2,101):
        for b in range(2,101):
            if not a**b in terms:
                terms.add(a**b)
    return len(terms)

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
    print(1634 == sum_pow(1634,4))
    
    num = 2
    total = 0
    times_not_found = 0
    # this wasn't a good way. on the forum there's a better way:
    # just check the maximum possible sum of quintics:
    # 1* 9**5 = 59049, which is greater than 9 (max 1-digit number)
    # 6* 9**5 = 354294, which is smaller than 999999 (max 6-digit number)
    # 7* 9**5 = 59049, which is smaller than 9999999
    # As the numbers go up and up, the chances get smaller and smaller of
    # having a number whose value is below the sum of quintics of its digits 
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

# proud of this one!
def euler031():
    import itertools
    values = [200,100,50,20,10,5,2,1]
    # how many ways to make dollar_amount with coins of these values?
    def cascade(values,dollar_amount):
        target_amount = dollar_amount
        if dollar_amount == 0:
            return 1
        if len(values) == 1:
            return 1
        combo_counter = 0
        while dollar_amount >= values[0]:
            dollar_amount -= values[0]
            combo_counter += cascade(values[1:],dollar_amount)
        combo_counter += cascade(values[1:],target_amount)
        return combo_counter
        
    return cascade(values,200)
    
def euler032():
    products = set()
    
    def test(a,b):
        s = str(a) + str(b) + str(a*b)
        if len(s) != 9:
            return False
        for i in range(1,10):
            if s.count(str(i)) != 1:
                return False
        return True

    for a in range(1,10):
        for b in range(1000,10000):
            if test(a,b) and a*b not in products:
                products.add(a*b)
                
    for a in range(10,100):
        for b in range(100,1000):
            if test(a,b) and a*b not in products:
                products.add(a*b)
    return sum(products)
            
def euler033():
    num = set()
    den = set()
    for a in range(10):
        for b in range(10):
            for c in range(10):
                try:
                    frac = (a*10 + b) / (b*10 + c)
                    if frac >= 1 or frac <= 0:
                        continue
                    test = a/c
                except ZeroDivisionError: # YOLO EAFP! GO PYTHON!
                    continue
                # no need to compensate for rounding error == GO PYTHON!
                #if frac >= test - 0.00000001 and frac < test + 0.00000001:
                if frac == test:
                    #print(str(a*10 + b),"/",str(b*10 + c)," == ",str(a),"/",str(c))
                    num.add(a*10 + b)
                    den.add(b*10 + c)
    n = 1
    for i in num:
        n *= i
    d = 1
    for i in den:
        d *= i
    plist = generate_primes(n, True)
    for i in plist:
        if i > n or i > d:
            break
        while (n % i == 0 and d % i == 0):
            n //= i
            d //= i
    return d

def euler034():
    # find maximum
    FACS = dict()
    FACS[0] = 1
    for i in range(1,10):
        FACS[i] = i * FACS[i-1]
    x = 1
    limit = FACS[9]
    while 10**x < limit:
        x += 1
        limit += FACS[9]
    retval = 0
    for i in range(3,limit):
        a = sum([FACS[int(l)] for l in str(i)])
        if a == i:
            retval += a
    return retval

def euler035():
    circular_primes = set()
    plist = generate_primes(1000000, True)
    def ror(i):
        s = str(i)
        return s[1:] + s[0]
    
    for p in plist:
        if p in circular_primes:
            continue
        orig_p = str(p)
        p_set = set()
        p_set.add(p)
        next_p = ror(p)
        is_circular = True
        while next_p != orig_p:
            this_p = int(next_p)
            if not check_prime(this_p,plist):
                is_circular = False
                break
            p_set.add(this_p)
            next_p = ror(next_p)
        
        if is_circular:
            circular_primes.update(p_set)
    return len(circular_primes)

def euler036():
    return sum( [ i for i in range(1,1000000,2) if test_palindrome(str(i)) and test_palindrome(str(bin(i))[2:]) ] )

def euler037():
    tpr = set()
    plist = generate_primes(10000)
    i = 4
    while len(tpr) < 11:
        p = plist[i]
        s = str(p)
        i += 1
        if i >= len(plist):
            plist = generate_primes(len(plist)+10000,False,plist)
        if not check_prime(int(s[0]),plist) or not check_prime(int(s[-1]),plist):
            continue
        #print(s + " passed initial.")

        failed = False
        
        sltr = s[1:]
        while len(sltr) > 1:
            if not check_prime(int(sltr),plist):
                failed = True
                break
            sltr = sltr[1:]
        if failed:
            continue
        #print(s + " passed ltr.")
        
        srtl = s[:-1]
        while len(srtl) > 1:
            if not check_prime(int(srtl),plist):
                failed = True
                break
            srtl = srtl[:-1]
        if failed:
            continue
        #print(s + " passed rtl.")
        tpr.add(p)
            
    print(tpr)
    return sum(tpr)
        
def euler038():
    m = 918273645
    i = 0
    def iterate(inp):
        i = inp + 1
        if str(i)[0] != '9':
            i = int("9" + str(i))
        return i
            
    while i < 99999:
        s = str(i)
        j = 2
        while len(s) < 9:
            s += str(i*j)
        if int(s) > m and test_pandigital(s):
            m = int(s)
        i = iterate(i)
    
    return m    
        
def euler039():
    # right angle triangle
    # the two other angles must add up to 90
    # all three sides must be integral to be considered a solution
    # which value of p <= 1000 has the most solutions?

    # my man pythagoras gonna hook me up
    # a^2 + b^2 = c^2
    # a < c
    # b < c
    # a + b + c = p

    # This is a brutally brute force attack on math
    # This takes way too long, too...
    # I refuse to use sqrt(). This can be solved without it.
    perms = dict()
    for a in range(1,1001):
        for b in range(a,1001):
            csq = a*a + b*b
            c = b + 1
            while csq > c*c:
                c += 1
            p = a + b + c
            if p > 1000:
                break
            if not a*a + b*b == c*c:
                continue
            
            if not p in perms:
                perms[p] = 1
            else:
                perms[p] += 1
    m = 0
    mp = 0
    for key,val in perms.items():
        if val > m:
            m = val
            mp = key
    return mp
                
def euler040():
    s = "."
    n = 1
    while(len(s) <= 1000000):
        s += str(n)
        n += 1
    r = 1
    print(s[12])
    print(s[11])
    print(s[10])
    print(s[9])
    print(len(s))
    print(n)
    for i in range(7):
        print("r: %i * %i (s[%i])" % (r,int(s[10**i]),10**i))
        r *= int(s[10**i])
    return r

def euler041():
    m = 2143

    for n in range(4,10):
        a = [ x for x in range(1,n+1) ]
        if a[-1] % 2 == 0:
            continue
        for i in range(get_nth_factorial(len(a))):
            b = permute(i,a)
            s = ""
            for j in b:
                s += str(j)

            if check_prime_slow(int(s)):
                m = int(s)
    return m



def euler042():
    with open("p042_words.txt","r") as file:
        tnums = set()
        r = 0
        for i in range(1,45):
            tnums.add(get_nth_triangle_number(i))
        p042_words = [w.strip('"') for w in file.read().split(',')]
        for word in p042_words:
            s = 0
            for letter in word:
                s += ord(letter) - ord('A') + 1
            if s in tnums:
                r += 1
        return r

def euler043():
    r = 0
    a = [x for x in range(10)]
    
    def has_properties(b):
        divisors = [7,11,13,17]
        passed = True
        if b[3] % 2 > 0:
            return False
        if (b[2]+b[3]+b[4]) % 3 > 0:
            return False
        if b[5] % 5 > 0:
            return False
        substr = ''.join([str(c) for c in b[4:]])
        for tester in range(4):
            sub = int(substr[tester:tester+3])
            if sub % divisors[tester] > 0:
                passed = False
                break
        return passed
    if not has_properties(list([int(x) for x in "1406357289"])):
        print("ERROR IN TESTING FUNCTION")
        return 
    for l in permute_iter(a):
        if has_properties(l):
            r += int(''.join([str(c) for c in l]))
    return r

def euler044():
    pent_list = set()
    max_pent = get_nth_pentagon_number(2)
    max_n = 2
    pent_list.add(get_nth_pentagon_number(1))
    pent_list.add(max_pent)
    found = False
    i = 2
    D = 0
    while not found:
        pk = get_nth_pentagon_number(i)
        i += 1
        D = pk
        while max_pent < (pk*2):
            max_n += 1
            max_pent = get_nth_pentagon_number(max_n)
            pent_list.add(max_pent)
        for pj in pent_list:
            if pj >= pk:
                continue
            if (pk - pj) in pent_list:
                if (pj + pk) in pent_list and D > (pk-pj):
                    D = pk-pj
                    found = True
    return D

def euler045():
    ti = 285
    tn = get_nth_triangle_number(ti)
    pi = 165
    pn = get_nth_pentagon_number(pi)
    hi = 143
    hn = get_nth_hexagonal_number(hi)
    found = False
    while not found:
        hi += 1
        hn = get_nth_hexagonal_number(hi)
        while(pn < hn):
            pi += 1
            pn = get_nth_pentagon_number(pi)
        if pn > hn:
            continue
        while(tn < hn):
            ti += 1
            tn = get_nth_pentagon_number(ti)
        if tn > hn:
            continue
        found = True
    return (tn,ti)
        
def euler046():
    from time import time_ns
    from math import sqrt
    i = 7
    time_in_gen = time_ns()
    plist = generate_primes(100000)
    # This is an interesting way to deal with reusing calculations...
    # but it's not really worth it
    
    #sqset = set([2])
    #sqmax = 2
    #sqidx = 1
    time_in_gen = time_ns() - time_in_gen
    gen_calls = 1
    found = False
    while not found:
        try:
            i += 2
            if check_prime(i,plist):
                continue
            if i > plist[-1]*plist[-1]:
                tig = time_ns()
                plist = generate_primes(len(plist)+100000,False,plist)
                time_in_gen += (time_ns()-tig)
                gen_calls += 1
            is_goldbach = False
            for prime in plist:
                if prime >= i:
                    break
                test = i - prime
                # while test > sqmax:
                #     sqidx += 1
                #     sqmax = 2*sqidx*sqidx
                #     sqset.add(sqmax)
                test //= 2
                sq = 1
                while sq*sq < test:
                    sq += 1
                if sq*sq == test:
                    is_goldbach = True
                    break
                
                #if test in sqset:
                #    is_goldbach = True
                #    break
                
            if not is_goldbach:
                return i
        except KeyboardInterrupt as k:
            print("Current number:",i)
            print("Max prime:",plist[-1]," Time spent generating:",time_in_gen*0.000001,"in %i calls" % gen_calls)
            if input("Exit? y/n ")[0] == 'y':
                raise k
            else:
                i -= 2

def euler047():
    found = False
    i = 10
    pset = generate_primes(10000)
    pmax = 13
    consecutive_length = 0
    contest = 2
    while not found:
        if i > pset[-1]*2:
            pset = generate_primes(len(pset)+10000,False,pset)
        itest = i
        fset = set()
        for piter in pset:
            while not itest % piter:
                fset.add(piter)
                itest //= piter
            if itest == 1 or piter > i*2:
                break
        if len(fset) == contest:
            consecutive_length += 1
            if consecutive_length == contest:
                print(contest,"starts at",i-contest+1)
                if contest == 4:
                    found = True
                    return i-3
                contest += 1
        else:
            consecutive_length = 0
        i += 1

def euler048():
    s = 0
    for i in range(1,1001):
        s += (i**i) % (10**10)
        s %= (10**10)
    return s

def euler049():
    plist = generate_primes(10000,True)
    start_prime = 0
    while plist[start_prime] < 1000:
        start_prime += 1
    pset = set(plist[start_prime:])
    # remove test case
    pset.remove(1487) 
    pset.remove(4817) 
    pset.remove(8147) 
    for prime in pset:
        for interval in range(2,3331,2):
            if prime + 2*interval >= 10000:
                break
            if prime + interval in pset and prime + 2*interval in pset:
                p1 = str(prime)
                p2 = str(prime + interval)
                p3 = str(prime + (2*interval))
                passed = True
                for i in range(10):
                    c = str(i)
                    p1c = p1.count(c)
                    if p1c != p2.count(c) or p1c != p3.count(c):
                        passed = False
                        break
                if passed:
                    return str(prime) + str(prime+interval) + str(prime+ (2*interval))
        
