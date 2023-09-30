#TLE_TC: O(n^3)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
      n = len(nums) 
      for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
              if [nums[i] < nums[k] < nums[j]:
                return True
      return False

#TLE_TC: O(n^2)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
      #TC: O(n^2)
      n = len(nums) 
      left_min = nums[0] 
      for j in range(1, n):
        for k in range(j+1, n):
          if left_min < nums[k] < nums[j]:
            return True 
        
        left_min = min(left_min, nums[j])
        
      return False
        
