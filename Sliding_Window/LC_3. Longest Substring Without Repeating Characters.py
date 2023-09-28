class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      
      d = {}; res = 0; l = 0
      
      for r in range(len(s)):
        while s[r] in d:
          del d[s[l]]
          l += 1
        d[s[r]] = 1
        res = max(res, r - l + 1)
      
      return res
        
