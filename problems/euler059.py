# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:20:28 2021

@author: db_wi
"""

def euler059():
    with open("static/p059_cipher.txt") as file:
        buffer = file.read().split(',')
        from numpy import bitwise_xor
        from string import ascii_lowercase
        search_terms = ["he","it","an","on","of","or","is"]
        result = None
        result_confidence = 0
        result_key = None
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
        return sum(ord(c) for c in result)