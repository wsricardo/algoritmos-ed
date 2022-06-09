# Linked list
class Node:
    
    def __init__(self, data=None,
    	 next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return '%s :-> %s'%(self.data, self.next)

class LinkedList:
    """
        Linked list class.
        Atributes
            _size - list size (private variable)
            head - pointer start for head of list
        Properties
            size
        Functions
            insert
            insert_in_index
            remove
            search

    """
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
        
        if self.head==None:
            self.head = Node(data)
        else:
            while pointer.next != None:
                pointer = pointer.next

            pointer.next = Node(data)
            
        self._size = self._size + 1
      
        
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
        self._size = self._size + 1 
        
    def remove(self, index):
        
        pointer = self.head
        count = 0
        
        if self.head == None:
            raise BaseException("Empty List")
            
        else:
            
            if index > self._size:
                raise BaseException('Index out range!')
            
            while count <= index - 1 :
                if count == index - 1:
                    count = count + 1
                    poster = pointer.next
                    del(pointer.next)
                    pointer.next = poster.next
                    self._size -= 1
                else:
                    pointer = pointer.next
                    count = count + 1
                
            
            pointer = poster
            
    def search(self, elem):
        """
            Search by element 'elem'.
            If found return position, pos variable;
            if not found return -1.
        """
        pos = 0
        pointer = self.head 
        
        while pointer.next != None:
            if pointer.data == elem:
                return pos
            else:
                pointer = pointer.next
                pos = pos + 1
        
        return -1
            
def helpMan():
    print('\n\n')
    print("*HELP*")
    print(18*"-")
    print("\n\n")
    return help(LinkedList)

if __name__=='__main__':
    l = LinkedList()
    l.insert( 2)
    l.insert(7)
    l.insert(13)
    l.insert_in_index(2, 21)
    print('> ', l)
    l.insert_in_index(index=1, elem=35)
    
    print('> ',l) 
    print('size l', l.size)
    print('len function ', len(l))
    l.remove(2)
    print('> ',l)
    print('New lenght of list ', len(l))
    print('search element 21 pos ', l.search(21) )
    #helpMan()
    
    
