# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:54:17 2021

@author: db_wi
"""

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
    return max(best_path[-1])
