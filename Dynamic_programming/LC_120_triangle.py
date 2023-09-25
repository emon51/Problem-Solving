class Solution(object):
    def minimumTotal(self, T):
        n = len(T)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        
        def f(r, c):
            if r == n-1:
                return T[r][c]
            if dp[r][c] != -1:
            	return dp[r][c]
            val = T[r][c]+min(f(r+1, c), f(r+1,c+1))
            dp[r][c] = val 
            return val 
            
        ans = f(0,0)
        return ans