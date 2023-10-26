#TLE, TC; O(n*n)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      z
      for k in range(1, max(piles) +1):
        time = 0 
        for b in piles: 
          time += math.ceil(b / k) 
        if time <= h:
          return k 
#==================================================================================#

#Accepted, TC: O(nlogn)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      
      l, r = 1, max(piles)
      
      while l <= r:
        mid = l + (r - l) // 2 
        time = 0 
        for b in piles:
          time += math.ceil(b / mid)
        if time <= h:
          res = mid
          r = mid - 1 
        else:
          l = mid + 1 
      return res
