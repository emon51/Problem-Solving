class Solution:
    def partitionString(self, s: str) -> int:
        seen = set(); res = 0;
        for ch in s:
            if ch in seen:
                res += 1
                seen = set()
            seen.add(ch)
        
        res += 1 if seen else 0
        return res

        
