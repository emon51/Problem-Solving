#Function to return the ceil of given number in BST.

#class Node:
#    def _init_(self,val):
#        self.key = val
#        self.left = None
#        self.right = None

class Solution:
    def findCeil(self,root, inp):
        
        res = -1 
        cur = root
        while cur:
            if cur.key == inp:
                return cur.key
            elif inp < cur.key:
                res = cur.key
                cur = cur.left
            else:
                cur = cur.right
        
        return res
            
            