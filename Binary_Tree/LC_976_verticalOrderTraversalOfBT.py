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
        