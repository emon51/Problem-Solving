#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        
        dp = [[-1 for _ in range(N)] for _ in range(N)]
        
        def _valid(i, j):
            return i >= 0 and i < N and j >=0 and j < N
        
        def f(r, c):
            if not _valid(r, c):
                return 0
            if r == N-1:
                return Matrix[r][c]
            if dp[r][c] != -1:
                return dp[r][c]
            val = Matrix[r][c] + max(f(r+1, c-1), f(r+1, c), f(r+1, c+1))
            dp[r][c] = val
            return val
            
        res = 0    
        for c in range(N):
            res = max(res, f(0, c))
        return res
            

