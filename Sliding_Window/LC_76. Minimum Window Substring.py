#TLE
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        prev_len = float("inf")
        res = ""
        for i in range(len(s)):
            d = Counter(t)
            for j in range(i, len(s)):
                if s[j] in d:
                    d[s[j]] -= 1
                    if d[s[j]] == 0:
                        del d[s[j]]
                if not d:
                    if (j - i + 1) < prev_len:
                        res = s[i:j + 1]
                        prev_len = j - i + 1
        return res

#Accepted

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tcount = Counter(t)
        window = {}
        minlen = float('inf')
        res = ''
        reqcount, currcount = len(tcount), 0
        l = 0

        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in tcount and window[ch] == tcount[ch]:
                currcount += 1
            
            while currcount == reqcount:
                if (r - l + 1) < minlen:
                    minlen = (r - l + 1)
                    res = s[l: r + 1]
                
                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    currcount -= 1
                l += 1
        return res
                
