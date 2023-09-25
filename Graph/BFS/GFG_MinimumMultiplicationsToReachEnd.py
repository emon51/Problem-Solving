#GFG: Minimum Multiplications to reach End

#User function Template for python3

from typing import List
from collections import deque
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
       q = deque()
       q.append((start, 0))
       vis = set()
       vis.add(start)
    
       while q:
           p, step = q.popleft()
           if p == end:
              return step
           for num in arr:
              next_val = (p * num) % 10**5
              if next_val not in vis:
                 q.append((next_val, step + 1))
                 vis.add(next_val)
       return -1