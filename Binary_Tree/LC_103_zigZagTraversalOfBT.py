# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      
      if not root:
        return 
      
      zigzag = 0
      q = deque() 
      q.append(root) 
      res = []
      while q:
        cur = []
        for _ in range(len(q)):
          p = q.popleft() 
          cur.append(p.val)
          if p.left:
            q.append(p.left) 
          if p.right:
            q.append(p.right)
        if zigzag:
          res.append(cur[::-1])
        else:
          res.append(cur)
        zigzag ^= 1
        
      return res