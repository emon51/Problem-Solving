# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
      
      if not root:
        return 
      
      q = deque() 
      q.append((root, 0, 0)) 
      d = {} 
      
      while q:
        p, x, y = q.popleft() 
        if x in d:
          d[x].append((p.val, y))
        else:
          d[x] = [(p.val, y)]
          
        if p.left:
          q.append((p.left, x - 1, y + 1))
        if p.right:
          q.append((p.right, x +1, y + 1))
      
      #print(d) 
      
      res = [] 
      
      for key in sorted(d):
        #print(key, sorted(d[key], key = lambda c: c[0]))
        #sorted with corresponding y-value then weight 
        cur = sorted(d[key], key = lambda c: (c[1], c[0]))
        cur = [val for val, y in cur] 
        res.append(cur)
      
      #print(res)
      return res


#Coding Ninjas: https://www.naukri.com/code360/problems/vertical-order-traversal_920533?leftPanelTabValue=PROBLEM
'''
Problem statement
Given a binary tree, return the vertical order traversal of the values of the nodes of the given tree.

For each node at position (X, Y), (X-1, Y-1) will be its left child position while (X+1, Y-1) will be the right child position.

Running a vertical line from X = -infinity to X = +infinity, now whenever this vertical line touches some nodes, we need to add those values of the nodes in order starting from top to bottom with the decreasing ‘Y’ coordinates.

Note:
If two nodes have the same position, then the value of the node that is added first will be the value that is on the left si
'''

from collections import deque, defaultdict

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def verticalOrderTraversal(root):
    if not root:
        return []

    q = deque()
    node_map = defaultdict(list)
    q.append((root, 0))  # (node, vertical distance
    
    while q:
        node, x = q.popleft()
        node_map[x].append(node.data)
        
        if node.left:
            q.append((node.left, x - 1))
        if node.right:
            q.append((node.right, x + 1))
    
    res = []
    for key in sorted(node_map):
        li = node_map[key]
        for val in li:
            res.append(val)
    
    return res

        
