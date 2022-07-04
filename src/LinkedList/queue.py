# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:47:42 2022

@author: wsric
"""

class Node:
    def __init__(self, data=None):
        self.data = data 
        self.ref = None
        
    def __repr__(self):
        return "%s -> %s "%(+ self.data, self.ref )
    

class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self._size = 0
    
    @property 
    def size(self):
        return self._size
    
    def __len__(self):
        return self._size
        
    def __repr__(self):
        return "%s"%( self.data)
        
    def insert(self, item):
        return 0
    
    def remove(self):
        return 0
    

if __name__=="__main__":
    
    pass
    
    