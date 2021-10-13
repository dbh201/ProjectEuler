# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:17:31 2021

@author: db_wi
"""

import struct
class FileHeader():
    load_string = str
    header_size = int
    field_names = list[str]
    values = dict
    
    def __init__(self,lstr,names):
        self.load_string = lstr
        self.field_names = tuple(names)
        self.values = dict()
        
    def save_header(self,file_handle):
        c = file_handle.tell()
        v = [ self.values[i] for i in self.field_names ]
        file_handle.seek(0)
        file_handle.write(struct.pack(self.load_string,v))
        file_handle.seek(c)
        
    def load_header(self,file_handle):
        c = file_handle.tell()
        file_handle.seek(0)
        a = struct.unpack(
            self.load_string,
            file_handle.read(
                struct.calcsize(self.load_string)
                )
            )
        for i in range(len(a)):
            self.values[self.field_names[i]] = a[i]
        file_handle.seek(c)
    
    def __getitem__(self,key):
        return self.values[key]
    
    def __setitem__(self,key,val):
        self.values[key]=val
        
    def __delitem__(self,key):
        raise Exception("Cannot delete elements from a file header!")
        
        
        
    
    