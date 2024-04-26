

def solve(n, edges) -> bool:
    adj = {u: [] for u in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    vis = set()

    def dfs(u, par):
        vis.add(u)
        for v in adj[u]:
            if v not in vis:
                if dfs(v, u):
                    return True
            else:
                if v != par:
                    return True
        


    for u in range(n):
        if u not in vis:
            if dfs(u, -1):
                return True
    return False
