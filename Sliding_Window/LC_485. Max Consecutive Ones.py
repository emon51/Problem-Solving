class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      
      nums.append(0)
      n = len(nums); l = 0; r = 0; res = 0
      while r < n:
        if nums[r] == 0:
          res = max(res, r - l)
          l = r
          while l < n and nums[l] == 0:
            l += 1
          r = l
          continue
        r += 1
      return res
          
        
        
