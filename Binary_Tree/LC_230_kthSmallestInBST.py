# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      
      #After inorder traversal in bst, we will get all the nodes in sorted(ascending) manner;
      
      def inorder(root):
        if root.left:
          inorder(root.left) 
        arr.append(root.val) 
        if root.right:
          inorder(root.right) 
          
      arr = [] 
      inorder(root)
      
      return arr[k-1]