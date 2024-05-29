
'''
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
      if not root:
        return 0
      res=0 
      q=deque() 
      q.append(root)
      while q: 
        p=q.popleft() 
        res+=1 
        if p.left:
          q.append(p.left) 
        if p.right: 
          q.append(p.right)
      return res




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return 0 
            l = dfs(root.left)
            r = dfs(root.right)
            return 1 + l + r
        
        return dfs(root)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def leftHeight(node):
            ht = 0 
            while node:
                ht += 1
                node = node.left 
            return ht
        
        def rightHeight(node):
            ht = 0 
            while node:
                ht += 1
                node = node.right
            return ht

        def dfs(root):
            if not root:
                return 0 
            lh = leftHeight(root)
            rh = rightHeight(root)
            if lh == rh:
                return (2 ** lh -1)
            else:
                return 1 + dfs(root.left) + dfs(root.right)
        
        return dfs(root)
