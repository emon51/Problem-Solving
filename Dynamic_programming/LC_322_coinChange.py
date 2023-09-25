"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""
#TLE _01
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
      
      res = float("inf")
      
      def fun(i, k, p = 0, dp = {}):
        nonlocal res
        if k == 0:
          res = min(res, p)
          return 
        if i == len(coins) or k < 0:
          return 
        if (i, k) in dp:
          return dp[(i, k)] 
        #pick
        fun(i, k - coins[i], p + 1)
        #notPick 
        fun(i + 1, k, p)
        
      fun(0, amount)
      return res if res != float("inf") else - 1
      
#TLE_02
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
      
      def fun(i, k, p = 0):
        if k == 0:
          return p
        if i == len(coins) or k < 0:
          return float("inf")
        
        pick = fun(i, k - coins[i], p + 1)
        notPick = fun(i + 1, k, p)
        return min(pick, notPick)
      
      
      res = fun(0, amount)
      return res if res != float("inf") else - 1
        
 #MLE(Memory Limit Exceeded)
 class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
      
      def fun(i, k, p = 0, dp = {}):
        if k == 0:
          return p
        if i == len(coins) or k < 0:
          return float("inf")
        if (i, k, p) in dp:
          return dp[(i, k, p)]
        
        pick = fun(i, k - coins[i], p + 1, dp)
        notPick = fun(i + 1, k, p, dp)
        val = min(pick, notPick)
        dp[(i, k, p)] = val 
        return val
      
      
      res = fun(0, amount)
      return res if res != float("inf") else - 1
      
#Optimal ✓✓✓
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      
      def fun(i, k, dp = {}):
        if k == 0:
          return 0 
        if i == len(coins) or k < 0:
          return float("inf") 
        if (i, k) in dp:
          return dp[(i, k)]
        
        pick = 1 + fun(i, k - coins[i]) 
        notPick = fun(i + 1, k) 
        val = min(pick, notPick)
        dp[(i, k)] = val 
        return val
      
      res = fun(0, amount)
      return res if res != float("inf") else -1
        
        
        
        