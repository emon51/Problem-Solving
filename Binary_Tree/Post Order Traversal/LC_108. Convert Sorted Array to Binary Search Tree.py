

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def fun(arr, l, r):
            if l > r:
                return None 
            mid = l + (r - l) // 2
            root = TreeNode(arr[mid])
            root.left = fun(arr, l, mid - 1)
            root.right = fun(arr, mid + 1, r)
            return root 
        
        return fun(nums, 0, len(nums) - 1)






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
      
      def fun(arr):
        if not arr:
          return None 
        mid = len(arr) // 2 
        root = TreeNode(val = arr[mid]) 
        root.left = fun(arr[:mid]) 
        root.right = fun(arr[mid + 1:]) 
        return root 
      
      return fun(nums)
        
