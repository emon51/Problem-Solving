#DFS
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''

class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        
        def dfs(root):
            if not root:
                return 0
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            return max(left, right)
        
        return dfs(root)

#BFS
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''

from collections import deque
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        
        q = deque()
        q.append((root, 1)) #node, level
        
        while q:
            p, lev = q.popleft()
            if p.left:
                q.append((p.left, lev + 1))
            if p.right:
                q.append((p.right, lev + 1))
                
        return lev
            
        

