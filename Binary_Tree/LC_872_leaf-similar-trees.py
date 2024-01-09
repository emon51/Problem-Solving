# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return []
            res = []
            if not root.left and not root.right:
                res += [root.val]
            res += dfs(root.left)
            res += dfs(root.right)
            return res

        r1 = dfs(root1)
        r2 = dfs(root2)
        return r1 == r2
            
