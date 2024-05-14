'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''

#Brute Force
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        res = float('-inf')
        n = len(nums)
        for i in range(n):
            sm = 0 
            for j in range(i, n):
                sm += nums[j]
                if (j - i + 1) == k:
                    res = max(res, sm / (j - i + 1))
        return res


        

#Sliding Window
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        res = float('-inf')
        sm = 0
        l = 0
        
        for r, num in enumerate(nums):
            sm += num 
            if (r - l + 1) == k:
                res = max(res, sm / k)
                sm -= nums[l]
                l += 1
        return res
        
