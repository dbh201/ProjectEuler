# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:09:45 2021

@author: db_wi
"""
import logging
logging.basicConfig(level=logging.INFO)
from eulermanager import EulerManager

if __name__ == "__main__":
    euler = EulerManager()
    finished = False
    while not finished:
        try:
            start_from = input("Problem to start from:")
            if start_from == '':
                start_from = None
            else:
                start_from = int(start_from)
            stop_at = input("Problem to stop at:")
            if stop_at == '':
                stop_at = None
            else:
                stop_at = int(stop_at)
            finished = True
        except ValueError:
            print("Please input an integer")
    print("SOLVING EVERYTHING!!!!")
    euler.solve_all(start_from,stop_at)