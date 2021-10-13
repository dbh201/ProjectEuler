# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:19:32 2021

@author: db_wi
"""

# proud of this one!
def euler031():

    values = [200,100,50,20,10,5,2,1]
    # how many ways to make dollar_amount with coins of these values?
    def cascade(values,dollar_amount):
        target_amount = dollar_amount
        if dollar_amount == 0:
            return 1
        if len(values) == 1:
            return 1
        combo_counter = 0
        while dollar_amount >= values[0]:
            dollar_amount -= values[0]
            combo_counter += cascade(values[1:],dollar_amount)
        combo_counter += cascade(values[1:],target_amount)
        return combo_counter
        
    return cascade(values,200)