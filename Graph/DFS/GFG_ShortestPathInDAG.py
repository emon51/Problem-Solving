#GFG: Shortest path in Directed Acyclic Graph
#User function Template for python3

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = {u: [] for u in range(n)}
        for u, v, w in edges:
            adj[u].append([v, w])
        
        vis = [0] * n 
        stk = []
        def topoSort(src):
            vis[src] = 1
            for v, w in adj[src]:
                if not vis[v]:
                    topoSort(v)
            stk.append(src) 
        #source node 0
        topoSort(0)
        res = [float("inf")] * n 
        res[0] = 0
        
        while stk: 
            u = stk.pop()
            for v, w in adj[u]:
                res[v] = min(res[u] + w, res[v]) 
        
        for i, v in enumerate(res):
            if v == float("inf"):
                res[i] = -1
        
        return res