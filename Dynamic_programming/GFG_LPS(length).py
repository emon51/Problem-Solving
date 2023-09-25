"""
Given a String, find the longest palindromic subsequence.

NOTE: Subsequence of a given sequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements

Example 1:

Input:
S = "bbabcbcab"
Output: 7
Explanation: Subsequence "babcbab" is the
longest subsequence which is also a palindrome.
"""
#Brute Force 
class Solution:

    def longestPalinSubseq(self, S):
        def fun(i, j):
            if i > j:
                return 0 
            if i == j:
                return 1 
            if S[i] == S[j]:
                return 2 + fun(i+1, j-1)
            else:
                return max(fun(i+1, j), fun(i, j-1))
        
        return fun(0, len(S)-1)
              
              
#Optimal 
class Solution:

    def longestPalinSubseq(self, S):
        def fun(i, j, dp = {}):
            if (i,j) in dp:
                return dp[(i, j)]
            if i > j:
                return 0 
            if i == j:
                return 1 
            if S[i] == S[j]:
                return 2 + fun(i+1, j-1)
            val = max(fun(i+1, j), fun(i, j-1))
            dp[(i, j)] = val 
            return val
        return fun(0, len(S)-1)
              
              
              