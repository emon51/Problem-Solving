# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1, num2 = 0, 0
        
        arr1, arr2 = [], []
        
        curr1 = l1 
        while curr1:
            arr1.append(curr1.val)
            curr1 = curr1.next
        
        curr2 = l2
        while curr2:
            arr2.append(curr2.val)
            curr2 = curr2.next 
            
        for n in arr1[::-1]:
            num1 = num1 * 10 + n
        
        for n in arr2[::-1]:
            num2 = num2 * 10 + n
        
        num = num1 + num2
        if num == 0:
            return ListNode(0)
        
        head = None; tail = None
        while num:
            val = num % 10
            node = ListNode(val)
            if not head:
                head = node 
                tail = head
            else:
                tail.next = node 
                tail = node
            num //= 10
         
        return head
        
        
