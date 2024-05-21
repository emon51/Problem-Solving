
'''
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
'''

#Solution_1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      
      arr = [] 
      cur = head 
      while cur:
        arr.append(cur.val) 
        cur = cur.next 
      
      l, r = 0, (n := len(arr)) - 1
      while l < r:
        if arr[l] != arr[r]:
          return False 
        l, r = l + 1, r - 1 
      return True 


#Solution_2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def findMid(head):
            dummy = ListNode(0)
            dummy.next = head
            slow, fast = dummy, head
            while fast and fast.next:
                slow = slow.next 
                fast = fast.next.next 
            return slow

        mid = findMid(head)
        prev = mid 
        curr = mid.next
        mid.next = None
        while curr:
            tmp = curr.next 
            curr.next = prev
            prev = curr
            curr = tmp 
        
        curr1, curr2 = head, prev
        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next 
            curr2 = curr2.next 
        return True
        
        



#Solution_3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def findMid(head):
            slow, fast = head, head
            while fast and fast.next and fast.next.next:
                slow = slow.next 
                fast = fast.next.next 
            return slow

        mid = findMid(head)
        prev = mid 
        curr = mid.next
        mid.next = None
        while curr:
            tmp = curr.next 
            curr.next = prev
            prev = curr
            curr = tmp 
        
        curr1, curr2 = head, prev
        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next 
            curr2 = curr2.next 
        return True
        
        
