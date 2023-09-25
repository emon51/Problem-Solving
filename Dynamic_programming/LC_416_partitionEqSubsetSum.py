
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
      
      target = sum(nums) / 2
      
      def f(i, k):
        if k == 0:
          return True
        if i == len(nums)-1:
          return k == nums[-1]
        pick = f(i + 1, k - nums[i]) 
        notPick = f(i + 1, k) 
        return pick or notPick
      
      return f(0, target)

      
        
        