class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
      
      res = 0; l = 0
      d = {}
      for r in range(len(nums)):
        if not d and nums[r] == 0:
          d[0] = r
        #another zero found out
        elif nums[r] == 0:
          #update result 
          res = max(res, r - l - 1)
          l = d[0] + 1
          #update 0's index.
          d[0] = r
      
      return max(res, r - l)
        
