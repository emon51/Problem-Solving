"""
#Leetcode: 115_Distinct subsequence
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
"""

#Brute Force 
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
      
      def fun(i, j):
        if j >= len(t):
          return 1 
        if i >= len(s):
          return 0 
        if s[i] == t[j]:
          return fun(i+1,j+1) + fun(i+1, j)
        else:
          return fun(i+1, j)
        
      return fun(0, 0)
      
#Optimal 
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
      
      def fun(i, j, dp = {}):
        if (i, j) in dp:
          return dp[(i, j)]
        if j >= len(t):
          return 1 
        if i >= len(s):
          return 0 
        if s[i] == t[j]:
          val = fun(i+1,j+1) + fun(i+1, j)
          dp[(i, j)] = val 
          return val 
        else:
          return fun(i+1, j)
        
      return fun(0, 0)
        
        