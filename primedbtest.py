# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:24:09 2021

@author: db_wi
"""
from euler_common.primes import PrimeDB
import cProfile
import pstats
with cProfile.Profile() as pr:
    p = PrimeDB(10001)
print("Stats:")
stats = pstats.Stats(pr)
stats.dump_stats(filename="primedb2.prof")