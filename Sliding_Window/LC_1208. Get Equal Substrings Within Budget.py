class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
      
      n = len(s); res = 0; l = 0; r = 0
      
      cost = 0
      while r < n:
        cost += abs(ord(s[r]) - ord(t[r]))
        while cost > maxCost:
          cost -= abs(ord(s[l]) - ord(t[l]))
          l += 1
        res = max(res, r - l + 1)
        r += 1
      return res
          
