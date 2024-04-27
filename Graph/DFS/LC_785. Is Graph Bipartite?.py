
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        vis = {}

        def dfs(u, flag):
            vis[u] = flag
            for v in graph[u]:
                if v not in vis:
                    if dfs(v, not flag) == False:
                        return False
                else:
                    if vis[v] == flag:
                        return False
        
        for u in range(len(graph)):
            if u not in vis:
                if dfs(u, True) == False:
                    return False
        return True        
