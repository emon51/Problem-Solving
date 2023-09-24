class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums); 
        
        l, r = 0, 1 
        
        while r < n:
          if nums[l] != nums[r]:
            nums[l+1] = nums[r] 
            l = l + 1
          r += 1
        return l + 1