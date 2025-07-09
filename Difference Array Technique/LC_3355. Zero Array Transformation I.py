
#Problem link: https://leetcode.com/problems/zero-array-transformation-i/

#Brute Force 
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        n = len(nums)
        for l, r in queries:
            for i in range(l, r + 1):
                nums[i] -= 1 if nums[i] > 0 else 0
        return sum(nums) == 0
        

#Optimal
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        n = len(nums)
        diffarr = [0] * n
        for l, r in queries:
            diffarr[l] += 1 
            if (r + 1) < n:
                diffarr[r + 1] -= 1 

        for i in range(1, n):
            diffarr[i] += diffarr[i - 1]
        
        for i in range(n):
            nums[i] -= diffarr[i]
            if nums[i] < 0:
                nums[i] = 0
        return sum(nums) == 0
        
