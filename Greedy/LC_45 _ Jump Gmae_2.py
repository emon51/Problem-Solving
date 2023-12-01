#Using BFS

from collections  import deque
class Solution:
    def jump(self, nums: List[int]) -> int:

        q = deque()
        q.append((0, 0)) #index, jump
        n = len(nums)
        vis = set()
        while q:
            index, jump = q.popleft()
            if index == (n-1):
                return jump
            for i in range(1, nums[index]+1):
                if (index+i) < n and (index+i) not in vis:
                    q.append((index+i, jump+1))
                    vis.add(index+i)

            


      
