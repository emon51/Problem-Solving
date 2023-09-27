class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
      
      if not k:
        return 0 
      
      n = len(nums)
      res = 0
      #cumulative product
      cp = 1
      l = 0
      for r in range(n):  
        cp *= nums[r]
        while l <= r and cp >= k:
          cp //= nums[l]
          l += 1
        res += (r - l + 1)
      return res
