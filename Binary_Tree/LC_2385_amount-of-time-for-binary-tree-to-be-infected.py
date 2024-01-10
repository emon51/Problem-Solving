# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        adj = defaultdict(list)
        q = deque()
        q.append(root)
        while q:
            p = q.popleft()
            if p.left:
                adj[p.val].append(p.left.val)
                adj[p.left.val].append(p.val)
                q.append(p.left)
            if p.right:
                adj[p.val].append(p.right.val)
                adj[p.right.val].append(p.val)
                q.append(p.right)
        
        q = deque()
        q.append([start, 0])
        vis = set()
        vis.add(start)

        while q:
            p, time = q.popleft()
            for ngh in adj[p]:
                if ngh not in vis:
                    q.append([ngh, time + 1])
                    vis.add(ngh)
        return time
            
            

                
        
