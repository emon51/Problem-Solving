class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Brute force, TC: O(n), SC:O(n) 
        
        non_zero_arr = []
        n = len(nums) 
        
        for i in range(n):
          if nums[i]:
            non_zero_arr.append(nums[i])
        
        i = 0 
        j = 0
        while i < n and j < len(non_zero_arr):
          nums[i] = non_zero_arr[j] 
          i += 1 
          j += 1 
        
        while i < n:
          nums[i] = 0
          i += 1
        
    
            
#TC: O(n), SC: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        l, r = 0, 0 
        
        while r < n:
          if nums[r]:
            nums[l] = nums[r]
            l += 1 
          r += 1 
        
        while l < n:
          nums[l] = 0 
          l += 1 
        
        
