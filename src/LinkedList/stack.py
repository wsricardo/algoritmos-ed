# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:06:56 2022

@author: Wandeson Ricardo
Blog: https://wsricardo.blogspot.com
"""

class Node:
    def __init__(self, data = 0, ant = None ):
        self.data = data
        self.ant = ant
        
    def __repr__(self):
        return "%s -> %s "%(+ self.data, self.ant) 
    
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    @property
    def size(self):
        return self._size
    
    def __len__(self):
        return self._size
    
    def __len__(self):
        """Retorna tamanho da pilha"""
        return self._size
    
    def __repr__(self):
        pointer = self.top
        s = ''
        top = 'top > '
        tab = len(top)
        s += top + str( pointer.data ) +'\n'
        pointer = pointer.ant 
        while pointer != None:
            s = s + tab*' '  + str(pointer.data) + '\n'
            pointer = pointer.ant
         
        return s
            
    
    def push(self, item):
        novo_no = Node(item)
        novo_no.ant = self.top 
        self.top = novo_no
        self._size = self._size + 1
            
    
    def pop(self):
        self.top = self.top.ant
        self._size = self._size - 1
        
        return 0
    
    def peek(self):
        
        return self.top 
    
    
if __name__ == "__main__":
    
    l = Stack()
    l.push(12)
    l.push(3)
    l.push(87)
    print(l)
    print("Size stack: {}\n".format(  len(l) ) )
    l.pop()
    print(l)
    l.peek()