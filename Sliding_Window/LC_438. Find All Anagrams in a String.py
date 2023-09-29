class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
      
      res = [] 
      
      p_hash = {} 
      for ch in p:
        p_hash[ch] = p_hash.get(ch, 0) + 1
        
      s_hash = {} 
      l = 0
      for r in range(len(s)):
        s_hash[s[r]] = s_hash.get(s[r], 0) + 1 
        
        if r >= len(p) - 1:
          if s_hash == p_hash:
            res.append(l)
          s_hash[s[l]] -= 1 
          if s_hash[s[l]] == 0:
            #s_hash.pop(s[l])
            del s_hash[s[l]]
          l += 1
            
      return res
      
