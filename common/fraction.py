# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 18:56:20 2021

@author: db_wi
"""
from .primedb import PRIME_DB
class Fraction():
    def __init__(self,numer=0,denom=1,autosimplify=True):
        self.autosimplify=autosimplify
        if type(numer) == self.__class__:
            self.n = numer.n
            self.d = numer.d
            self._simplify()
        else:
            self.n = int(numer)
            self.d = int(denom)
            self._simplify()
        if self.d == 0:
            raise ValueError("Cannot have 0 as denominator, stupid")
        
        
            
    def _reduce(self,i):
        while self.n%i == 0 and self.d%i == 0:
            self.n //= i
            self.d //= i
            
    def _simplify(self):
        if self.d < 0:
            self.d *= -1
            self.n *= -1
        if self.autosimplify:
            self.simplify()   
            
    def simplify(self):
        global PRIME_DB
        for p in PRIME_DB.db:
            if p > self.d:
                return
            self._reduce(p)
            
    def remainder(self):
        return Fraction(self.n%self.d,self.d)

    def __gt__(self,r):
        if type(r) == int:
            return self.n > r*self.d
        elif type(r) == self.__class__:
            return (self.n*r.d) > (r.n*self.d)
        else:
            raise TypeError("Can't compare %s and Fraction" % type(r))
    def __eq__(self, r):
        if type(r) == int:
            return self.n == r*self.d
        elif type(r) == self.__class__:
            return (self.n*r.d) == (r.n*self.d)
        else:
            raise TypeError("Can't compare %s and Fraction" % type(r))
    def __lt__(self,r):
        return not (self > r or self == r)
    
    def __le__(self,r):
        return not self > r
    def __ge__(self,r):
        return self > r or self == r
    def __ne__(self, r):
        return not self == r
        
    def __int__(self):
        return self.integer()
    def integer(self):
        return self.n // self.d
    def __iadd__(self,r):
        if type(r) == int:
            self.n += self.d*r
            self._simplify()
            return self
        elif type(r) == self.__class__:
            if self.d == r.d:
                self.n += r.n
            else:
                d = self.d*r.d
                n = (self.n*r.d)+(r.n*self.d)
                self.d = d
                self.n = n
                self._simplify()
            return self
        else:
            raise TypeError("Can't iadd %s with Fraction" % type(r))
    def __isub__(self,r):
        if type(r) == int:
            return self.__iadd__(-r)
        elif type(r) == self.__class__:
            r.n *= -1
            self.__iadd__(r)
            r.n *= -1
            return self
        else:
            raise TypeError("Can't isub %s with Fraction" % type(r))
    def __add__(self,r):
        if type(r) == int:
            return self.__class__(self.n+self.d*r,self.d)
        elif type(r) == self.__class__:
            o = self.__class__(self)
            if o.d == r.d:
                o.n += r.n
            else:
                d = o.d*r.d
                n = (o.n*r.d)+(r.n*o.d)
                o.d = d
                o.n = n
                o._simplify()
            return o
        else:
            raise TypeError("Can't add %s to Fraction" % type(r))
    
    def __sub__(self,r):
        if type(r) == int:
            return self.__class__(self.n-(self.d*r),self.d)
        elif type(r) == self.__class__:
            o = self.__class__(self)
            d = o.d*r.d
            n = (o.n*r.d)-(r.n*o.d)
            o.d = d
            o.n = n
            o._simplify()
            return o
        else:
            raise TypeError("Can't sub %s from Fraction" % type(r))
    def __mul__(self,r):
        if type(r) == int:
            return self.__class__(self.n*r,self.d)
        elif type(r) == self.__class__:
            o = self.__class__(self)
            o.d*=r.d
            o.n*=r.n
            o._simplify()
            return o
        else:
            raise TypeError("Can't mult %s with Fraction" % type(r))
            
    def inverse(self):
        o = self.d
        self.d = self.n
        self.n = o
        self._simplify()
        return self
    
    def __truediv__(self,r):
        return self*r.inverse()
    def __str__(self):
        if self.d == 1:
            return str(self.n)
        return "%i/%i" % (self.n,self.d)