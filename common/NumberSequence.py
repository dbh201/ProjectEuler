# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:52:51 2021

@author: db_wi
"""

from abc import abstractmethod

class NumberSequence:
    def __init__(self):
        self.cache = dict()
        self.cache_enabled = True
    
    # @abstractmethod
    # def get_generator(self,first=None,last=None):
    #     """Retrieve a generator for this sequence."""
    #     pass
    
    @abstractmethod
    def get_nth(self,n):
        """Retrieve the nth member of this sequence."""
        pass
    
    @abstractmethod
    def get_inv(self,y):
        """Retrieve the integer index of the member y, or None if not integer."""
        pass
    
    def clear_cache(self):
        self.cache.clear()
        self.set.clear()
    
    def enable_cache(self,enabled):
        if not enabled:
            self.clear_cache()
        self.cache_enabled = enabled
        
    def _verify_x_val(self,x):
        if x < 0:
            return None
        xi = int(x)
        if xi == x:
            return xi
        return None

class CachelessNumberSequence(NumberSequence):
    def __init__(self):
        self.cache_enabled = False
    def clear_cache(self):
        pass
    def enable_cache(self,enabled):
        pass
    def __contains__(self,y):
        x = self.get_inv(y)
        if not x: return False
        if x[1] < 0: return False
        if int(x[1]) == x[1]: return True
        return False
    
    