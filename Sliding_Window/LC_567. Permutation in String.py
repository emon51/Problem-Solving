from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_window = Counter(s1)
        window = {}
        l = 0
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            if (r - l + 1) == len(s1):
                if window == s1_window:
                    return True
                else:
                    window[s2[l]] -= 1
                    if window[s2[l]] == 0:
                        del window[s2[l]]
                    l += 1
        return False
                
