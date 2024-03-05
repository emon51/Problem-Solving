

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
class MyStack:
    def __init__(self):
        self.head = None
        
    def push(self, val):
        
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        
    def pop(self):
        
        if not self.head:
            return -1
        poppedData = self.head.data
        self.head = self.head.next
        return poppedData
        
