#User function Template for python3
from collections import deque 
class Solution:
    def minTime(self, root, target):
        #finding the target node using level order traversal(bfs)
        # and make parent reference to move up from target node.
        tar_node = None 
        parent = {}
        q = deque() 
        q.append(root)
        
        while q:
            p = q.popleft() 
            if p.data == target:
                tar_node = p 
            if p.left:
                q.append(p.left)
                parent[p.left] = p
            if p.right:
                q.append(p.right)
                parent[p.right] = p
                
                
        #BFS
        if not tar_node:
            return 0
            
        q = deque() 
        vis = set()
        q.append((tar_node, 0)) # target_node, time
        vis.add(tar_node)
        
        while q:
            p, t = q.popleft()
            if p.left and p.left not in vis:
                q.append((p.left, t + 1))
                vis.add(p.left)
            if p.right and p.right not in vis:
                q.append((p.right, t + 1))
                vis.add(p.right)
            if p in parent and parent[p] not in vis:
                q.append((parent[p], t + 1)) 
                vis.add(parent[p])
        return t
        
