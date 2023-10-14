class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Idea sort the array, after sorting the array, nums[i] == i if not return i
        #sort the array using cyclic sort algorithm.
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] < n and nums[i] != i:
                #correct_index
                ci = nums[i]
                nums[i], nums[ci] = nums[ci], nums[i]
            else:
                i  += 1
        
        #after sorting check, nums[i] = i or not, if not return i
        for i, val in enumerate(nums):
            if i != val:
                return i
            
        return n
    
    #TC: O(n), SC: O(1)
