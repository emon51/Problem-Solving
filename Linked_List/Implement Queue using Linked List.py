
#Expected Time Complexity: O(1).
#Expected Auxiliary Space: O(1).

class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self):
        
        self.head = None
        self.tail = None
    
    def push(self, val): 
        
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
         
    def pop(self):
        
        if not self.head:
            return -1
        
        poppedData = self.head.data
        self.head = self.head.next
        
        if not self.head:
            self.tail = None
        
        return poppedData
