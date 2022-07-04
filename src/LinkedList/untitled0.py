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
        
    def __repr__(self):
        return "%s"%( self.data)
        
    def insert(self, item):
        return 0
    
    def remove(self):
        return 0
    
    