class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def fun(i):
            if i in dp:
                return dp[i]
            if i == (n - 1):
                return cost[i]
            if i >= n:
                return 0
            l = cost[i] + fun(i + 2)
            r = cost[i] + fun(i + 1)
            val = min(l, r)
            dp[i] = val
            return val
            
        n = len(cost)
        dp = {}
        return min(fun(0), fun(1))
