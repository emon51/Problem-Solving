"""
#Leetcode: 1143
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""
#Brute Force
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        #Brute Force, finds all subsequences of text1 and text2 and check.
        def fun(i, s, textNo, p = ''):
            if i == len(s):
                if textNo == 1:
                    set1.add(p)
                else:
                    set2.add(p)
                return
            fun(i + 1, s, textNo, p + s[i])
            fun(i + 1, s, textNo, p)



        set1, set2 = set(), set()
        fun(0, text1, 1)
        fun(0, text2, 2)

        res = 0 
        for s in set1:
            if s in set2:
                res = max(res, len(s))
        
        return res

        
#TLE
class Solution:
    def longestCommonSubsequence(self, s, t):
      
      def fun(i, j):
        if i >= len(s) or j >= len(t):
          return 0 
        #match 
        if s[i] == t[j]:
          return 1 + fun(i + 1, j + 1)
        #not match
        l = fun(i, j + 1) 
        r = fun(i + 1, j) 
        return max(l, r) 
      
      return fun(0, 0) 
      
#Optimal 
class Solution:
    def longestCommonSubsequence(self, s, t):
      
      def fun(i, j, dp = {}):
        if i >= len(s) or j >= len(t):
          return 0 
        if (i, j) in dp:
          return dp[(i, j)]
        #match 
        if s[i] == t[j]:
          return 1 + fun(i + 1, j + 1)
        #not match
        l = fun(i, j + 1) 
        r = fun(i + 1, j) 
        val = max(l, r) 
        dp[(i, j)] = val 
        return val
      
      return fun(0, 0) 
    
        
    
        
