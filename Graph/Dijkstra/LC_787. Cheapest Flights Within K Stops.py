
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {u: [] for u in range(n)}
        for u, v, w in flights:
            adj[u].append((v, w))
        
        dist = {u: float('inf') for u in range(n)}
        dist[src] = 0

        q = deque()
        q.append((src, 0, 0)) #src, step, cost

        while q:
            u, step, cost = q.popleft()
            for v, w in adj[u]:
                if step <= k and (cost + w) < dist[v]:
                    dist[v] = cost + w
                    q.append((v, step + 1, cost + w))
        
        return dist[dst] if dist[dst] != float('inf') else -1

        
