# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      
      N = 0; curr = head 
      
      while curr:
        N += 1 
        curr = curr.next
        
      if N == 1:
        return 
      if (N - n) == 0: #have to remove headnode.
        return head.next
      
      i = 0 
      curr = head
      while curr:
        i += 1 
        if i == (N - n):
          curr.next = curr.next.next
        curr = curr.next 
      return head
        
