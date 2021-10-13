# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:44:08 2021

@author: db_wi
"""

def euler068():
    # Topography:
#      g
#        \ 
#         -b-    h
#       /     \ /  
#      a       c
#     / \     / 
#    f   e - d - i
#         \
#          j
#    
    # assigning positions for each number, lettered a-j (a=first,j=tenth)
    # linkages forming lines are as follows:
    # fab,gbc,hcd,ide,dej = 5 lines

    # numbers and their positions
    pos = [x for x in range(1,11)]
    # number groups must all add up to the same number
    groups = [
        (5,0,1),
        (6,1,2),
        (7,2,3),
        (8,3,4),
        (9,4,5)
        ]
    vals = dict()
    max_result = 0
    # ugly brute force? this is like sudoku, so there's a much better way...
    # ITERATOR BROKEN :()
    for iteration in permute_iter(pos):
        val = iteration[5] + iteration[0] + iteration[1]
        l = list()
        for group in groups:
            if iteration[group[0]] + iteration[group[1]] + iteration[group[2]] != val:
                val = -1
                break
            l.append(
                (iteration[group[0]],iteration[group[1]],iteration[group[2]])
                )
            
        if not val == -1:
            m = l.index(min(l))
            l = l[m:] + l[:m]
            try:
                vals[val].append(l)
            except KeyError:
                vals[val] = [l]
    print(vals)
    # ANOTHER brute force. I suck.
    for k in vals.keys():
        
        for iteration in vals[k]:
            s = ""
            for group in iteration:
                s += ''.join(str(i) for i in group)
            if len(s) != 16:
                break
            v = int(s)
            if v > max_result:
                max_result = v
    return max_result
    # a->b->c
    #  
    #
    #
    #