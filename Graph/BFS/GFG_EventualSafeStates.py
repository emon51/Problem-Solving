#GFG:Eventual Safe States

#User function Template for python3
from collections import deque 
from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        
        adj_rev = {node: [] for node in range(V)}
        indegree = [0] * V
        for parent in range(V):
            for children in adj[parent]:
                adj_rev[children].append(parent)
                indegree[parent] += 1
        
        q = deque() 
        safe_nodes = [0] * V
        
        for node in range(V):
            if indegree[node] == 0:
                q.append(node)
                
        while q:
            node = q.popleft()
            safe_nodes[node] = 1
            for ngh in adj_rev[node]:
                indegree[ngh] -= 1
                if indegree[ngh] == 0:
                    q.append(ngh)
        
        return [node for node in range(V) if safe_nodes[node]]