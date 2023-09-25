#User function Template for python3
from collections import deque 
class Solution:
    def shortestPath(self, edges, n, m, src):
        #make an adjency list from given edges
        adj = {u: [] for u in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
  
        #BFS
        q = deque() 
        vis = [0] * n
        q.append(src)
        vis[src] = 1
        
        distance = [0] * n
        distance[src] = 0
        
        while q:
            u = q.popleft() 
            for v in adj[u]:
                if not vis[v]: 
                    q.append(v) 
                    vis[v] = 1
                    distance[v] = distance[u] + 1 
        
        for node, d in enumerate(distance):
            if node != src and d == 0:
                distance[node] = -1
        
        return distance 