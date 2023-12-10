
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        
        heap = []
        for key, val in d.items():
            heapq.heappush(heap, [-val, key])
        
        res = ""
        block = None
        while heap:
            freq, char = heapq.heappop(heap)
            res += char
            freq += 1
            if block:
                heapq.heappush(heap, block)
            block = [freq, char] if freq != 0 else None
            
        return res if not block else ''
