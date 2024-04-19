
'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''

#TLE
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(l, r, n):
            if l == r == n:
                return True 
            if r == n:
                return False
            res = False
            if s[l: r + 1] in wordDict:
                res = res or dfs(r + 1, r + 1, n)
            res = res or dfs(l, r + 1, n)
            return res

        return dfs(0, 0, len(s))
        


#Accepted
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(l, r, n, memo = {}):
            if (l, r) in memo:
                return memo[(l, r)]
            if l == r == n:
                return True 
            if r == n:
                return False
            res = False
            if s[l: r + 1] in wordDict:
                res = res or dfs(r + 1, r + 1, n)
            res = res or dfs(l, r + 1, n)
            memo[(l, r)] = res
            return res

        return dfs(0, 0, len(s))
        
