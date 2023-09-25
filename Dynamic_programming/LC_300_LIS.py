"""
Leetcode: 300_LIS

Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
#TLE 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      
      def fun(i, prev = float("-inf")):
        if i == len(nums):
          return 0 
        pick = 0
        if nums[i] > prev:
          pick = 1 + fun(i + 1, nums[i]) 
        notPick = fun(i + 1, prev)
        return max(pick, notPick) 
    
      return fun(0)
        
#MLE 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      
      def fun(i, prev = float("-inf"), dp = {}):
        if i == len(nums):
          return 0 
        if (i, prev) in dp:
          return dp[(i, prev)]
        pick = 0
        if nums[i] > prev:
          pick = 1 + fun(i + 1, nums[i]) 
        notPick = fun(i + 1, prev)
        val = max(pick, notPick) 
        dp[(i, prev)] = val 
        return val
    
      return fun(0)
      
#MLE 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      
      def fun(i, prev = -1, dp = {}):
        if i == len(nums):
          return 0 
        if (i, prev) in dp:
          return dp[(i, prev)]
        pick = 0
        if prev == -1 or nums[i] > nums[prev]:
          pick = 1 + fun(i + 1, i, dp) 
        notPick = fun(i + 1, prev, dp)
        val = max(pick, notPick) 
        dp[(i, prev)] = val 
        return val
    
      return fun(0)
        
        