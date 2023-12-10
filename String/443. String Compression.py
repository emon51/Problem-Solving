class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        if n <= 1:
            return n
        
        pos = 0
        r = 0
        
        while r < n:
            char = chars[r]
            cnt = 1
            r += 1
            while r < n and chars[r] == char:
                r += 1
                cnt += 1
            chars[pos] = char
            pos += 1
            if cnt > 1:
                for num in str(cnt):
                    chars[pos] = num
                    pos += 1
                    
        return pos
