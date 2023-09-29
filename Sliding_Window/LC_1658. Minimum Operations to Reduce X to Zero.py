class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
      
      def func(arr, i, j, x, stp = 0, dp = {}):
        if (i, j, x, stp) in dp:
          return dp[(i, j, x, stp)]
        if x == 0:
          return stp
        if x < 0 or i > j:
          return float("inf")
        
        l = func(arr, i + 1, j, x - arr[i], stp + 1, dp) 
        r = func(arr, i, j - 1, x - arr[j], stp + 1, dp)
        val = min(l, r)
        dp[(i, j, x, stp)] = val 
        return val
      
      res = func(nums, 0, len(nums) - 1, x)
      return -1 if res == float("inf") else res
        
