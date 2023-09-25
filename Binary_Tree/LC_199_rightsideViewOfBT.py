# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
      
      if not root:
        return [] 
      
      #simple level order traversal, the LAST value of each level is the part of the required output;
      
      q = deque() 
      res = [] 
      q.append(root) 
      
      while q:
        cur = [] 
        for _ in range(len(q)):
          p = q.popleft() 
          cur.append(p.val) 
          if p.left:
            q.append(p.left) 
          if p.right:
            q.append(p.right)
        res.append(cur[-1]) 
        
      return res
      
      