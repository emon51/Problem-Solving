#User function Template for python3

from collections import deque
class Solution:
    
    #Function to check whether a Binary Tree is BST or not.                                                          
    def isBST(self, root):
    
        #BFS
        if not root:
            return True 
        
        q = deque() 
        s, e = float('-inf'), float('inf')
        q.append((root, s, e))
 
        while q: 
            p, s, e = q.popleft()
            if not (s < p.data < e):
                return False
            if p.left:
                q.append((p.left, s, p.data))
            if p.right:
               q.append((p.right, p.data, e))
        return True