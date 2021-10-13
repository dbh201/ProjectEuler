# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:51:51 2021

@author: db_wi
"""

def euler010():
    return sum(PRIME_DB.get_prime_list(max_prime=2000000))