#BFS
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        q.append(start)
        n = len(arr)
        vis = set()
        vis.add(start)
        
        while q:
            index = q.popleft()
            if arr[index] == 0:
                return True
            if (index + arr[index]) < n and (index + arr[index]) not in vis:
                q.append(index + arr[index])
                vis.add(index + arr[index])
            if (index - arr[index])>= 0 and (index - arr[index]) not in vis:
                q.append(index - arr[index])
                vis.add(index - arr[index])
        return False
        
