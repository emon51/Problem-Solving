"""
#Leetcode: 516_LPS
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
      
      def fun(i, j, dp = {}):
        if (i, j) in dp:
          return dp[(i, j)]
        if i > j:
          return 0 
        if i == j:
          return 1 
        if s[i] == s[j]:
          return 2 + fun(i+1, j-1)
        else:
          val = max(fun(i+1, j), fun(i, j-1))
          dp[(i, j)] = val 
          return val
      
      return fun(0, len(s)-1)