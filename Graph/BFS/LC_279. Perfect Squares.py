
#BFS

class Solution:
    def numSquares(self, n: int) -> int:

        q = deque()
        sqrs = [i*i for i in range(1, int(n ** 0.5) + 1)][::-1]
        q.append((n, 0))
        vis = set()

        while q:
            n, step = q.popleft()
            if n == 0:
                return step
            for sq in sqrs:
                if (n - sq) >= 0 and (n - sq) not in vis:
                    q.append((n - sq, step + 1))
                    vis.add(n - sq)
        return 0



    
