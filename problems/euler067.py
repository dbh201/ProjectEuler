# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:31:12 2021

@author: db_wi
"""

def euler067():
    with open("static/p067_triangle.txt","r") as file:
        s=file.read()
    layers = [[int(r) for r in l.strip().split(' ')] for l in s.split('\n')[:-1]]
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