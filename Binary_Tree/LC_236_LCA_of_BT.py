# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      
      #Brute force and Accepted 
      
      #Traverse root to p and store the path in p_arr, traverse root to q and store the path in q_arr after that traverse p_arr and q_arr simultaneously and checking p_arr[i] == q_arr[i] and last p_arr[i] == q_arr[i] satisfied element will be required output. 
      
      def dfs(root, target_node, arr = []):
        if root == target_node:
          arr.append(root)
          res.append(arr)
          return
        if root.left:
          dfs(root.left, target_node, arr + [root])
        if root.right:
          dfs(root.right, target_node, arr + [root])
        
      res = [] 
      dfs(root, p) 
      dfs(root, q) 
      
      p_arr, q_arr = res[0], res[1]
      
      i, j, m, n = 0, 0, len(p_arr), len(q_arr)
      
      while i < m and j < n:
        if p_arr[i] == q_arr[j]:
          res = p_arr[i] 
        i, j = i + 1, j + 1
      
      return res
      
#Optimal 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      
      def dfs(node):
        if not node or node in (p, q) :
          return node
        l = dfs(node.left) 
        r = dfs(node.right) 
        if l and r:
          return node
        else:
          return l or r 
        
      return dfs(root)
        
      
      
        