# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:06:56 2022

@author: Wandeson Ricardo
Blog: https://wsricardo.blogspot.com
"""
from copy import copy

class Node:
    def __init__(self, data = 0, next = None ):
        self.data = data
        self.next = next
        
    def __repr__(self):
        return "%s -> %s "%( self.data, self.next) 
       

    
class LinkedList:
    
    def __init__(self, head=None):
        self.head = head
        
    def __repr__(self):
        return "%s"%(self.head)
    
    def insert_end(self, elem):
        """
            Insere elemento no final da lista.
        """
        nova = self
        pointer = nova.head
        
        while pointer != None:
            if pointer.next == None:
                break
            else:
                pointer = pointer.next
            
        no = Node(elem)
        pointer.next = no
        nova.next = pointer
        print("pointer %s"%(pointer))
        return nova
    
    def insert_start(self, elem):
        """
        

        Parameters
        ----------
        elem : Node
            Node

        Returns
        -------
        nova : LinkedList
            Retorna uma lista nova com elemento inserido no inicio da lista.

        """
        nova = self
        novo_no = Node(elem)
        novo_no.next = nova.head
        nova.head = novo_no
        return nova
    
if __name__ == "__main__":
    no1 = Node(12)
    no2 = Node(1332)
    no3 = Node(123)
    no1.next = no2
    no2.next = no3
    l = LinkedList(head = no1)
    
    print("No1 lists {} ".format( no1 ) )
    print("Linked List \n {}".format(l))
    print("\nLinkedList inserted new element {}".format( l.insert_end(152245) ) )
    l.insert_start(13.45)
    print("Lnked List inserted in start %s"%(l))