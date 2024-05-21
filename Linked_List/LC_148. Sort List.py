'''
Given the head of a linked list, return the list after sorting it in ascending order.
Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 
Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
'''

#Brute Force(Accepted)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      arr=[]
      cur=head 
      while cur:
        arr.append([cur.val,cur]) 
        cur=cur.next 
      head,tail=None,None 
      arr.sort(key=lambda c : c[0])
      for val,node in arr:
        if not head:
          head=node 
          tail=node 
        else:
          tail.next=node 
          tail=node 
          tail.next=None 
      return head 
        
    
        
        
        

#Selection Sort(TLE)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #Selection Sort
        curr = head 
        while curr:
            minval = curr.val
            minNode = curr
            post = curr.next 
            while post:
                if post.val < minval:
                    minNode = post
                    minval = post.val
                post = post.next 
            if curr != minNode:
                curr.val, minNode.val = minNode.val, curr.val
            curr = curr.next
        
        return head


        

#Merge Sort(Accepted)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #Merge Sort 

        def _findMid(head):
            dummy = ListNode(0)
            dummy.next = head
            slow, fast = dummy, head
            while fast and fast.next:
                slow = slow.next 
                fast = fast.next.next 
            return slow
        
        def _merge(l1, l2):
            head = None
            tail = head
            while l1 and l2:
                if l1.val <= l2.val:
                    tmp = l1.next 
                    l1.next = None
                    if not head:
                        head = l1
                        tail = l1
                    else:
                        tail.next = l1
                        tail = l1
                    l1 = tmp
                else:
                    tmp = l2.next 
                    l2.next = None
                    if not head:
                        head = l2
                        tail = l2
                    else:
                        tail.next = l2
                        tail = l2 
                    l2 = tmp
            tail.next = l1 or l2
            return head
            

        
        def mergeSort(head):
            if not head or not head.next:
                return head
            mid = _findMid(head)
            leftHead, rightHead = head, mid.next
            mid.next = None
            L = mergeSort(leftHead)
            R = mergeSort(rightHead)
            return _merge(L, R)

        return mergeSort(head)




































        
