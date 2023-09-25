# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Solution_01
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
      
      st = set();
      q = deque();
      q.append(root);
      
      while q:
        
        p = q.popleft();
        if p.val in st:
          return True;
        st.add(k - p.val);
        
        if p.left:
          q.append(p.left);
        if p.right:
          q.append(p.right);
      return False
      
#Solution_02 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
      
      #Inorder traversal in bst always gives us node shorted(asc) in nature.
      
      def inorder(root):
        if root.left:
          inorder(root.left) 
        arr.append(root.val) 
        if root.right:
          inorder(root.right)
          
      arr = [] #node's value
      inorder(root) 
      
      l, r = 0, len(arr) - 1 
      while l < r:
        sm = arr[l] + arr[r]
        if sm == k:
          return True 
        elif k < sm:
          r -= 1 
        else:
          l += 1
      return False
        
        
        
        