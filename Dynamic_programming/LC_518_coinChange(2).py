"""
#Leetcode: 518_Coin_Change(2)

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""


#TLE
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
      
      def fun(i, k):
        if k == 0:
          return 1 
        if i == len(coins) or k < 0:
          return 0 
        pick = fun(i, k - coins[i]) 
        notPick = fun(i + 1, k) 
        return pick + notPick
      
      return fun(0, amount)
    
        
#Optimal 
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
      
      def fun(i, k, dp = {}):
        if k == 0:
          return 1 
        if i == len(coins) or k < 0:
          return 0 
        if (i, k) in dp:
          return dp[(i, k)]
        pick = fun(i, k - coins[i]) 
        notPick = fun(i + 1, k) 
        val = pick + notPick
        dp[(i, k)] = val 
        return val 
      
      return fun(0, amount)
    
        