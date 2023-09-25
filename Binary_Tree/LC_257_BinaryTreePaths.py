# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
      
      def dfs(root, p = ""):
        if not root.left and not root.right:
          p += "->" + str(root.val) 
          res.append(p[2:])
          return
        if root.left:
          dfs(root.left, p + "->" + str(root.val)) 
        if root.right:
          dfs(root.right, p + "->" + str(root.val))
      
      res = []
      dfs(root) 
      return res
          
      