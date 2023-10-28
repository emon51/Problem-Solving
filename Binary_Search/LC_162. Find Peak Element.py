class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
      
      n = len(nums) 
      #handle when n=1 or n=2.
      if n == 1:
        return 0 
      if nums[0] > nums[1]:
        return 0
      if nums[n-1] > nums[n-2]:
        return n-1
      
      l, r = 1, n-2
      
      while l <= r:
        m = l + (r - l) // 2
        if  nums[m-1] < nums[m] > nums[m+1]:
          return m 
        #we are in incresing part.
        if nums[m-1] < nums[m]:
          l = m + 1
        #we are in decresing part.
        else:
          r = m - 1
    
