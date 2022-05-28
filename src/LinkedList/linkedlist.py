# Linked list
class Node:
    
    def __init__(self, data=None,
    	 next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return '%s :-> %s'%(self.data, self.next)

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self._size = 0
        
    def __repr__(self):
        return '[%s]'%(self.head)
        
    def __len__(self):
        return self._size
        
    @property
    def size(self):
        return self._size
           
    def insert(self, data):
        pointer = self.head
        nova = pointer 
        aux = None
        print('head pointer', pointer)
        
        if self.head==None:
            self.head = Node(data)
        else:
            while pointer.next != None:
                pointer = pointer.next

            pointer.next = Node(data)
            
        self._size = self._size + 1
      
        nova = pointer 
        print('size list', self._size)
        print(pointer)
        
    def insert_in_index(self, index, elem):
        pointer = self.head
        count = 0
        
        if index > self._size:
            raise BaseException('Index out range list')
            
        else:
            while count < index - 1:
                pointer = pointer.next
                count = count + 1
        
        no = Node(elem)
        no.next = pointer.next
        pointer.next = no    
            

if __name__=='__main__':
    l = LinkedList()
    l.insert( 2)
    l.insert(7)
    l.insert(13)
    l.insert_in_index(2, 21)
    
    print('> ',l) 
    print('size l', l.size)
    print('len function ', len(l))
    
    
    # Endereço de a
    #a = 2
    #print(id(a))
    