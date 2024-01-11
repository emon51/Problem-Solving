
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        q = deque()
        res = 0
        q.append([root, root.val, root.val]) #node, max_ancestor, min_ancestor
        while q:
            p, max_ancestor, min_ancestor = q.popleft()
            res = max(res, abs(max_ancestor - p.val), abs(min_ancestor - p.val))
            curr_max_ancestor = max(max_ancestor, p.val)
            curr_min_ancestor = min(min_ancestor, p.val)

            if p.left:
                q.append([p.left, curr_max_ancestor, curr_min_ancestor])

            if p.right:
                q.append([p.right, curr_max_ancestor, curr_min_ancestor])

        return res












        
