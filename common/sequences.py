# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 18:54:30 2021

@author: db_wi
"""
from .NumberSequence import NumberSequence,CachelessNumberSequence
from .theorems import quadratic_theorem
from math import sqrt



class TriangleNumberSequence(CachelessNumberSequence):
    def get_nth(self,n):
        return n*(n+1)//2
    
    def get_inv(self,y):
        x = quadratic_theorem(0.5,0.5,-y)[1]
        return self._verify_x_val(x)

# lol
class SquareNumberSequence(CachelessNumberSequence):
    def get_nth(self,n):
        return n*n
    
    def get_inv(self,y):
        try:
            x = sqrt(y)
        except ValueError:
            x = None
        return self._verify_x_val(x)
    
class PentagonalNumberSequence(CachelessNumberSequence):
    def get_nth(self,n):
        return n*((3*n)-1)//2
    
    def get_inv(self,y):
        x = quadratic_theorem(1.5, -0.5, -y)[1]
        return self._verify_x_val(x)

class HexagonalNumberSequence(CachelessNumberSequence):
    def get_nth(self,n):
        return n*((n*2)-1)
    
    def get_inv(self,y):
        x = quadratic_theorem(2,-1,-y)[1]
        return self._verify_x_val(x)
    
class HeptagonalNumberSequence(CachelessNumberSequence):
    def get_nth(self,n):
        return n*((5*n)-3)//2
    
    def get_inv(self,y):
        x = quadratic_theorem(2.5,-1.5,-y)[1]
        return self._verify_x_val(x)
    
class OctagonalNumberSequence(CachelessNumberSequence):
    def get_nth(self,n):
        return n*((3*n)-2)
    
    def get_inv(self,y):
        x = quadratic_theorem(3,-2,-y)[1]
        return self._verify_x_val(x)
    
class FactorialSequence(NumberSequence):
    def __init__(self):
        super().__init__()
        self.cache[0]=1
        self.cache[1]=1
        self.cache[2]=2
        self.max = 2
        
    def get_nth(self,n):
        if n in self.cache:
            return self.cache[n]
        if n < 0:
            raise ValueError("Factorial n value cannot be less than zero")
        self.cache[n] = n*self.get_nth(n-1)
        self.max = n
        return self.cache[n]
    
    def get_inv(self,y):
        # calculate and cache sequence until we're past the test value
        while self.cache[self.max] < y:
            self.get_nth(self.max+1)
        
        i = self.max
        while self.cache[i] > y:
            i -= 1
        if self.cache[i] == y:
            return i
        return None

class FibonacciSequence(NumberSequence):
    def __init__(self):
        super().__init__()
        self.cache[0]=0
        self.cache[1]=1
        self.cache[2]=1
        self.max = 2
        
    def get_nth(self,n):
        if n in self.cache:
            return self.cache[n]
        if n < 0:
            raise ValueError("Fibonacci n value cannot be less than zero")
        n_1 = self.get_nth(n-1)
        n_2 = self.get_nth(n-2)
        self.cache[n] = n_1 + n_2
        self.max = n
        return self.cache[n]
    
    def get_inv(self,y):
        while self.cache[self.max] < y:
            self.get_nth(self.max+1)
        i = self.max
        while self.cache[i] > y:
            i -= 1
        if self.cache[i] == y:
            return i
        return None
    
class PascalsTriangle():
    def __init__(self):
        self.array = [[1],[1,1]]
    def get_pos(self,layer,offset):
        try:
            return self.get_layer(layer)[offset]
        except IndexError:
            raise ValueError(
                "PascalsTriangle layer %i is only %i elements wide, but element %i requested" 
                % (layer,len(self.array[layer]),offset)
                )
    def get_layer(self,layer):
        while len(self.array) <= layer:
            self.generate_layer()
        return self.array[layer]
    def generate_layer(self):
        self.array.append([0 for x in range(len(self.array[-1])+1)])
        self.array[-1][0]=1
        self.array[-1][-1]=1
        for i in range(1,len(self.array[-1])-1):
            self.array[-1][i] = self.array[-2][i]+self.array[-2][i-1]
    