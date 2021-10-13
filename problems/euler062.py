# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:35:45 2021

@author: db_wi
"""


# INCOMPLETE - need better algo for permutation count
def euler062():
    def get_permutation_count(n,cubes,max_cube,max_idx):
        permutations = set()
        i = 0
        for iterator in permute_iter(str(n)):
            i += 1
            iter_int = int(''.join(iterator))
            while iter_int > max_cube:
                max_idx += 1
                max_cube = max_idx**3
                cubes.add(max_cube)
            if iter_int in cubes:
                permutations.add(iter_int)
        return (len(permutations),cubes,max_cube,max_idx)

    cubes = set()
    cubes.add(1)
    max_cube = 1
    max_idx = 1
    done = True
    i = 2
    while not done:
        c = i**3
        permutations,cubes,max_cube,max_idx = get_permutation_count(c, cubes, max_cube, max_idx)
        if permutations == 5:
            return c
        i += 1
    return None