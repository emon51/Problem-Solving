# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.


#Using Queue

from collections import deque
def LeftView(root):
    
    if not root:
        return []
        
    q = deque()
    res = []
    q.append(root)
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            curr = node.data
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        res.append(curr)
    return res
    
