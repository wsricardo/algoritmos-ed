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
        self._table = None
    
    @property 
    def size(self):
        return self._size
    
    @property 
    def table(self):
        return self._table
    
    
    def __len__(self):
        return self._size
        
    def __repr__(self):
        pointer = self.start
        s = ''
        while pointer != None:
            s = s + str(pointer.data) + " -> " 
            pointer = pointer.ref 
            #print(pointer)
        s += 'None'  
        self._table = s
        
        return s
        
    def insert(self, item):
        pointer_novo_no = Node(item)
        
        # lista vazia; "end" e "start" apontam pro no None
        if self._size == 0:
            self.start = pointer_novo_no
            
            self.end = pointer_novo_no 
            
        else:
            
            self.end.ref = pointer_novo_no
            self.end = pointer_novo_no
        
        self._size = self._size + 1
    
    def remove(self):
        if self._size == 0:
            raise BaseException(f"Empty Queue. Class {self.__class__} Size: {self._size}")
        else:
            self.start = self.start.ref
    

if __name__=="__main__":
    l = Queue()
    l.insert(321)
    l.insert(1)
    l.insert(35)
    print(l)
    l.remove()
    print(l)
    q = Queue()
    q.remove()
    
    pass
    
    