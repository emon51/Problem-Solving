# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        
        while q:
            curr_max = float("-inf")
            for _ in range(len(q)):
                p = q.popleft()
                curr_max = max(curr_max, p.val)
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            res.append(curr_max)
            
        return res
