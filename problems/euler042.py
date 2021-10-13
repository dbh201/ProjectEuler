# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:29:11 2021

@author: db_wi
"""

def euler042():
    with open("static/p042_words.txt","r") as file:
        tnums = set()
        r = 0
        tri = TriangleNumberSequence()
        for i in range(1,45):
            tnums.add(tri.get_nth(i))
        p042_words = [w.strip('"') for w in file.read().split(',')]
        for word in p042_words:
            s = 0
            for letter in word:
                s += ord(letter) - ord('A') + 1
            if s in tnums:
                r += 1
        return r