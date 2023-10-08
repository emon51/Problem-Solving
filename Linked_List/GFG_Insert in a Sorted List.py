#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
#class Node:
#    def __init__(self, data):   # data -> value stored in node
#        self.data = data
#        self.next = None

class Solution:
    def sortedInsert(self, head1, key):
        # return head of edited linked list
        dummyHead = Node(data = 0)
        dummyHead.next = head1
        
        prev, curr = dummyHead, head1
        while curr and curr.data < key:
            prev = curr
            curr = curr.next
            
        newNode = Node(data = key)
        prev.next = newNode
        newNode.next = curr
        
        return dummyHead.next
