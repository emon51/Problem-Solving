

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = {u: [] for u in range(n)}
        for pair, w in zip(edges, succProb):
            u, v = pair
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        probs = {u: 0 for u in range(n)}
        probs[start] = 1

        q = deque()
        q.append((start, 1))

        while q:
            u, p = q.popleft()
            for v, w in adj[u]:
                if (p * w) > probs[v]:
                    probs[v] = p * w
                    q.append((v, probs[v]))
        
        return probs[end]
