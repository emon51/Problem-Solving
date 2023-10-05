"""
Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly k distinct characters. 

Example 1:

Input:
S = "aba", K = 2
Output:
3
Explanation:
The substrings are: "ab", "ba" and "aba".
"""
class Solution:
    def substrCount (self,s, k):
        atMostK = 0; atMostK_1 = 0; n = len(s)
        
        d = {}; l = 0
        for r in range(n):
            d[s[r]] = d.get(s[r], 0) + 1
            while len(d) > k:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    d.pop(s[l])
                l += 1
            atMostK += (r - l + 1)
            
        d = {}; l = 0;
        for r in range(n):
            d[s[r]] = d.get(s[r], 0) + 1
            while len(d) > (k - 1):
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    d.pop(s[l])
                l += 1
            atMostK_1 += (r - l + 1)
        
        return atMostK - atMostK_1
            
            
            
            
            
            
            
            
