class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
      res = 0; l = 0; d = {} 
      
      csm = 0 
      for r in range(len(nums)):
        
        while l <= r and nums[r] in d:
          csm -= nums[l]
          del d[nums[l]] 
          l += 1 
          
        csm += nums[r]
        d[nums[r]] = 1
        
        res = max(res, csm)
      
      return res
