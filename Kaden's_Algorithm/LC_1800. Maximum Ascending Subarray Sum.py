'''
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

 

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
Example 2:

Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
Example 3:

Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

'''

#Brute Force 
#TC: O(N*N); SC: O(1)
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        n, res = len(nums), 0 
        for i in range(n):
            csm = nums[i]
            j = i + 1
            while j < n and nums[j - 1] < nums[j]:
                csm += nums[j]
                j += 1
            res = max(res, csm)
        return res 
        

#Kaden's-Algorithm
#TC: O(N); SC: O(1)
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        res = nums[0]
        csm = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                csm += nums[i]
            else:
                csm = nums[i]
            res = max(res, csm)
        return res 

        
