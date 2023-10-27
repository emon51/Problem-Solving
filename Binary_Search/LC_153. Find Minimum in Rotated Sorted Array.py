class Solution:
    def findMin(self, nums: List[int]) -> int:
      
      l, r = 0, len(nums) - 1 
      res = float("inf")
      while l <= r:
        mid = l + (r - l) // 2
        #left part is sorted 
        if nums[l] <= nums[mid]:
          res = min(res, nums[l])
          #skip left part 
          l = mid + 1 
        #right part is sorted 
        else:
          res = min(res, nums[mid])
          #skip right part 
          r = mid - 1 
      return res
