class Solution:
    def integerBreak(self, n: int) -> int:
      
      def fun(tar, dp={}):
        if tar in dp:
          return dp[tar]
        if tar == 0:
          return 1
        if tar < 0:
          return -1
        res = 0
        for num in range(1, n):
          tmp = num * fun(tar - num)
          res = max(res, tmp)
        
        dp[tar] = res
        return res
        

      return fun(n)
        
