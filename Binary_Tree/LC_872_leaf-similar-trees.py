#DFS
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

#BFS_stack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a = self.bfs(root1)
        b = self.bfs(root2)
        if a == b:
            return True
        else:
            return False
    def bfs(self, node):
        hold = []
        if not node:
            return
        stack = [node]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                hold.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return hold
            
