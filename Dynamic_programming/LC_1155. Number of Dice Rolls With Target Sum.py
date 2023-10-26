#TLE
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
      def fun(n, sm = 0):
        if n == 0 and sm == target:
          return  1
        elif n == 0:
          return 0
        cnt = 0
        for i in range(1, k + 1):
          cnt += fun(n-1, sm+i)
        return cnt
      
      
      return fun(n)
#=============================================================================================#

#Accepted
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
      def fun(n, sm = 0, memo = {}):
        if (n, sm) in memo:
          return memo[(n, sm)]
        elif n == 0 and sm == target:
          return  1
        elif n == 0:
          return 0
        cnt = 0
        for i in range(1, k + 1):
          cnt += fun(n-1, sm+i)
        memo[(n, sm)] = cnt
        return cnt
      
      
      return fun(n) % (10**9 + 7)
      
        
             
          
                
      
        
             
