'''
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''

#Recursion/ Bactracking
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPal(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True 
        
        res = []
        n = len(s)
        def fun(i, p = []):
            nonlocal res, n
            if i == n:
                res.append(p)
                return 
            for j in range(i, n):
                if isPal(s[i: j + 1]):
                    fun(j + 1, p + [s[i: j + 1]])
        
        fun(0)
        return res

        
