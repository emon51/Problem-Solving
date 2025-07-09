
Problem link: 3356. https://leetcode.com/problems/zero-array-transformation-ii/description/

#Brute Force 
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        n = len(nums)
        k = 0 
        if sum(nums) == 0:
            return 0
            
        for si, ei, val in queries:
            k += 1
            for i in range(si, ei + 1):
                nums[i] -= val 
            if (sum([num for num in nums if num > 0])) == 0:
                return k
            
        return -1
        

#Optimal (Binary Search + Difference Array Technique)
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        if sum(nums) == 0:
            return 0

        l, r = 0, len(queries) - 1
        res = -1
        while l <= r:
            mid = l + (r - l) // 2 
            diffarr = [0] * len(nums)
            for si, ei, val in queries[: mid + 1]:
                diffarr[si] += val 
                if (ei + 1) < len(nums):
                    diffarr[ei + 1] -= val 
                  
            for i in range(1, len(nums)):
                diffarr[i] += diffarr[i - 1]
              
            temp = nums.copy()
          
            for i in range(len(nums)):
                temp[i] = max(0, temp[i] - diffarr[i])
              
            if sum(temp) == 0:
                res = mid + 1 #1 based count
                r = mid - 1
            else:
                l = mid + 1
            
        return res
        
