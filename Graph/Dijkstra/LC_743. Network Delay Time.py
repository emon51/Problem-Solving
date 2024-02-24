
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {u: [] for u in range(1, n + 1)}
        for u, v, w in times:
            adj[u].append((v, w))
        
        time = {u: float('inf') for u in range(1, n + 1)}
        time[k] = 0

        q = deque()
        q.append((k, 0))

        while q:
            u, t = q.popleft()
            for v, w in adj[u]:
                if (t + w) < time[v]:
                    time[v] = t + w
                    q.append((v, t + w))
        
        res = -1
        for u, t in time.items():
            if t == float('inf'):
                return -1
            res = max(res, t)
        
        return res
        
