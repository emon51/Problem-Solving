
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj) -> list:
        
        vis = [0] * V
        stk = []
        def dfs(node):
            vis[node] = 1 
            for v in adj[node]:
                if not vis[v]:
                    dfs(v)
            stk.append(node)
            
        for node in range(V):
            if not vis[node]:
                dfs(node)
                
        res = [] 
        while stk:
            res.append(stk.pop())
        return res