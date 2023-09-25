# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      
      q = deque() 
      q.append((root, 1)) 
      
      res = 0 
      
      while q:
        start = 0 
        for _ in range(len(q)):
          p, n = q.popleft() 
          if not start:
            start = n 
          if p.left:
            q.append((p.left, 2*n))
          if p.right:
            q.append((p.right, 2*n +1))
        res = max(res, n - start +1)
      
      return res
        