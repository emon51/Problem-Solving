
Poblem link: 847. Shortest Path Visiting All Nodes

from collections import deque 
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        n = len(graph)
        all_visited = (1 << n) - 1 #2^n - 1
        q = deque()
        vis = set()
        for node in range(n):
            q.append([node, 1 << node, 0])
            vis.add((node, 1 << node))
        
        while q:
            node, mask, path = q.popleft()
            if mask == all_visited:
                return path 
            for ngh in graph[node]:
                new_mask = mask | (1 << ngh)
                if (ngh, new_mask) not in vis:
                    q.append([ngh, new_mask, path + 1])
                    vis.add((ngh, new_mask))
        return -1
        

        
