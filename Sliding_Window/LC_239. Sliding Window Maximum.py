class Solution:
    from heapq import heappush, heappop
   
     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      
      res = []
      heap = []
      n = len(nums)
      
      for i in range(k):
        heappush(heap, [-nums[i], i])
      res.append(-heap[0][0])
      
      for i in range(k, n):
        heappush(heap, [-nums[i], i]) 
        while heap and (i - heap[0][1] + 1) > k:
          heappop(heap) 
        
        res.append(-heap[0][0])
      return res
        
        