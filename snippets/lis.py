# lis.py -- longest increasing subsequence; not my idea :(
# stolen from the below website:
# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
from typing import TypeVar, Optional, List, Any
def lis_len(inp: List) -> List:

    # Keep record of the smallest and largest values
    # and their associated sequences (so we don't have to
    # keep searching for them)
    smallest_end = (99999999, None) # Do this some other way, like with MAX_INT
    largest_end = (-1, None)
    lens = list()
    
    for i in range(len(inp)):
        try:
            if inp[i] <= lens[0]:
                # ignore duplicates
                if inp[i] == lens[0]:
                    continue
                
                # "start a new list of length 1"
                # lens[0] corresponds to the end value of the list
                # of length 1, and since we're only keeping end values
                # we can just replace it
                lens[0] = inp[i]
                continue
            
        except IndexError:
            # we have to start somewhere!
            lens.append(inp[i])
            continue
        
        if inp[i] >= lens[-1]:
            # Don't bother with duplicates
            if inp[i] == lens[-1]:
                continue

            # This equates to a "clone & extend"
            # so inp[i] is now the end value of the longest sequence
            lens.append(inp[i])
        
        else:
            # Find the sequence which has the largest value
            # that is still smaller than inp[i]
            
            # best candidate value 
            m = -1
            # index of sequence with this candidate
            m_idx = -1
            
            for s in range(len(lens)):

                # lens is already sorted, so we can break on this condition
                if lens[s] >= inp[i]:
                    break
                
                if lens[s] > m:
                    m = lens[s]
                    m_idx = s

            # "clone & extend", but we're only keeping the last element
            # so this equates to replacing m_idx+1 with the new value.
            try:
                lens[m_idx+1] = inp[i]
            except IndexError:
                # m_idx+1 didn't exist, so we have a new longest sequence
                lens.append(m)
    for l in range(len(lens)):
        print("{}: {}".format(l+1,lens[l]))
    return len(lens)


def lis_seq(inp: List) -> List:

    # Keep record of the smallest and largest values
    # and their associated sequences (so we don't have to
    # keep searching for them)
    smallest_end = (99999999, None) # Do this some other way, like with MAX_INT
    largest_end = (-1, None)
    seqs = dict()
    
    for i in range(len(inp)):
        if inp[i] <= smallest_end[0]:
            
            # Don't bother with duplicates
            if inp[i] == smallest_end[0]:
                 continue

            # Start a new sequence with this lowest value
            seqs[1] = [inp[i]]

            # update the efficiency variable
            smallest_end = (inp[i],1)
            
        elif inp[i] >= largest_end[0]:
            
            # Don't bother with duplicates
            if inp[i] == largest_end[0]:
                continue
            
            # This corresponds to the index of the longest sequence so far
            longest_seq_idx = max(seqs.keys())

            # "append" inp[i] and store in the sequence dictionary
            seqs[longest_seq_idx+1] = seqs[longest_seq_idx] + [inp[i]]

            # update the efficiency variable
            largest_end = (inp[i],longest_seq_idx+1)
        
        else:
            # Find the sequence which has the largest value
            # that is still smaller than inp[i]
            
            # best candidate value 
            m = -1
            # index (or length) of sequence with this candidate
            m_idx = -1

            
            # In the "strictly-increasing" test case,
            # duplicates are not allowed.
            # "non-decreasing" means duplicates are allowed.

            #dups = []
                
            for s in seqs.keys():
                if seqs[s][-1] > inp[i]:
                    continue
                # This if statement is to allow duplicates
                # if seqs[s][-1] == inp[i]:
                #     dups.append(s)
                if seqs[s][-1] > m:
                    m = seqs[s][-1]
                    m_idx = s

            # This loop appends duplicates
            #for s in dups:
            #    seqs[s+1] = seqs[s] + [inp[i]]
            

                
                    
            # at this point, we've checked every sequence
            # and the candidate can be considered fully tested

            # clone & extend
            seqs[m_idx+1] = seqs[m_idx] + [inp[i]]

            # update efficiency variables if necessary
            if m_idx+1 == smallest_end[1]:
                smallest_end = (inp[i],m_idx+1)
            if m_idx+1 == largest_end[1]:
                largest_end = (inp[i],m_idx+1)
    for s in seqs.keys():
        print("{}:{}".format(s,seqs[s]))
    return seqs[max(seqs.keys())]
TESTS = [
    [10,9,2,5,3,7,101,18],
    [0,1,0,3,2,3],
    [7,7,7,7,7,7,7],
    [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    ]

for test in TESTS:
    print("===" + str(test) + "===")
    r = lis_seq(test)
    print(r)
    r = lis_len(test)
    print(r)
