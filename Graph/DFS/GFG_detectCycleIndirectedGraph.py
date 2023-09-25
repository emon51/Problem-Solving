#User function Template for python3

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        vis, path_vis = set(), set();
        
        def dfs(node):
            vis.add(node)
            path_vis.add(node)
            for v in adj[node]:
                if v not in vis:
                    if dfs(v) == True:
                        return True 
                else:
                   if v in path_vis:
                        return True
            path_vis.remove(node)
            
            
        for node in range(V):
            if node not in vis:
                if dfs(node):
                    return True 
        return False
            