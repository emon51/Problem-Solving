"""
#Leetcode: 46_permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""

class Solution:
    def permute(self, nums):
      
      res = []
      def fun(i, p = []):
        if i >= len(nums):
          res.append(p)
          return 
        for j in range(len(p)+1):
          prev = p[:j] 
          post = p[j:] 
          s = prev + [nums[i]] + post 
          fun(i+1, s) 
      
      fun(0)
      return res
        