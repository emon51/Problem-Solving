

#Accepted
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        adj = {u: [] for u in range(n)}
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        heap = [(0, 0)] #cost, src
        times = [float('inf')] * n
        times[0] = 0
        ways = [0] * n
        ways[0] = 1

        while heap:
            t, u = heapq.heappop(heap)
            for v, w in adj[u]:
                if (w + t) < times[v]:
                    ways[v] = ways[u]
                    times[v] = w + t
                    heapq.heappush(heap, (times[v], v))
                elif (w + t) == times[v]:
                    ways[v] += ways[u]
                   
        return ways[n - 1] % (10 ** 9 + 7)
