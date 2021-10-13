# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:54:03 2021

@author: db_wi
"""

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