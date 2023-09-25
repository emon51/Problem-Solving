"""
#Leetcode: 76_Edit_Distance
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
#TLE
class Solution:
    def minDistance(self, s: str, t: str) -> int:
      
      def fun(i, j):
        if i >= len(s):
          return len(t) - j
        if j >= len(t):
          return len(s) - i
        if s[i] == t[j]:
          return fun(i+1, j+1)
        insert = 1 + fun(i, j+1)
        remove = 1 + fun(i+1, j) 
        replace = 1 + fun(i+1, j+1)
        return min(insert, remove, replace)
                         
      return fun(0, 0)
      
#Accepted 
class Solution:
    def minDistance(self, s: str, t: str) -> int:
      
      def fun(i, j, dp = {}):
        if (i, j) in dp:
          return dp[(i, j)]
        if i >= len(s):
          return len(t) - j
        if j >= len(t):
          return len(s) - i
        if s[i] == t[j]:
          return fun(i+1, j+1)
        insert = 1 + fun(i, j+1)
        remove = 1 + fun(i+1, j) 
        replace = 1 + fun(i+1, j+1)
        val = min(insert, remove, replace)
        dp[(i, j)] = val 
        return val 
      return fun(0, 0)