#Leetcode: 863_All Nodes Distance K in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
      
      #make parent reference to move up from target node
      parent = {} 
      q = deque() 
      q.append(root)
      
      while q:
        p = q.popleft()
        if p.left:
          q.append(p.left) 
          parent[p.left] = p
        if p.right:
          q.append(p.right)
          parent[p.right] = p 
          
      #BFS 
      q = deque() 
      vis = set() 
      q.append((target, k))
      vis.add(target) 
      res = []
      
      while q:
        p, d = q.popleft()
        if d == 0:
          res.append(p.val)
        if p.left and p.left not in vis:
          q.append((p.left, d - 1))
          vis.add(p.left) 
        if p.right and p.right not in vis:
          q.append((p.right, d - 1)) 
          vis.add(p.right) 
        if p in parent and parent[p] not in vis:
          q.append((parent[p], d - 1)) 
          vis.add(parent[p])
      
      return res
          
        
        