"""  list Node is as defined below:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""

# complete this function
# return head of list after swapping
class Solution:    
    def pairWiseSwap(self, head):
        dummyHead = Node(data = 0)
        dummyHead.next = head
        prev, a, b = dummyHead, head, head.next
        while a and b:
            tmp = b.next
            prev.next = b
            b.next = a
            a.next = tmp
            
            prev = a
            a = tmp
            b = a.next if a else None
        return dummyHead.next


