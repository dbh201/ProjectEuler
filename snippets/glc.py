def get_longest_cycle(l):
    i = 0
    j = 1
    k = 2
    r = []
    done = False
    for i in range(len(l)):
        for rm in range(2,(len(l)//2)+1-i):
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
                for d2 in range(rm):
                    if d != l[i+d2]:
                        good = True
                if good:
                    #print("Sequence good!")
                    r.append(rm)
                else:
                    #print("Sequence was a single digit.")
                    continue
    return min(r)
