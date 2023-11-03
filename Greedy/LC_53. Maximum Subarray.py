class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csm = 0
        res = float('-inf')
        
        for n in nums:
            csm += n 
            res = max(res, csm)
            if csm < 0:
                csm =  0
        return res

  #=====================================================================#
  class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      res = float('-inf'); csm = float("-inf")
      for n in nums: 
        csm = max(csm + n, n) 
        res = max(res, csm) 
      return res
        
