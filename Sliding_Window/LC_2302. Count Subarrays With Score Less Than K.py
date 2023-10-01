class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
      
      res = 0; l = 0; csm = 0;
      for r in range(len(nums)):
        csm += nums[r] 
        while csm * (r - l + 1) >= k:
          csm -= nums[l] 
          l += 1 
        
        res += (r - l + 1) 
      
      return res
        
