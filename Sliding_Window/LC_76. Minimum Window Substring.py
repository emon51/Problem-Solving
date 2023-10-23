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
