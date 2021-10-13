# -*- coding: utf-8 -*-

def euler001():
    r = 0
    for i in range(1000):
        if not (i % 3) or not (i % 5):
            r += i
    return r