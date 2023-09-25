#User function Template for python3

#class Node:
#    def _init_(self,val):
#        self.data = val
#        self.left = None
#        self.right = None
        
class Solution:
    def floor(self, root, x):
        
        res = -1 
        cur = root 
        while cur:
            if cur.data == x:
                return x 
            elif x < cur.data:
                cur = cur.left 
            else:
                res = cur.data
                cur = cur.right 
        return res
        