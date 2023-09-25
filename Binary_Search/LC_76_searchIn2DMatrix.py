"""
#Leetcode: 74_Search in a 2D matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""
#Using Binary Search
class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
      
      #helper_function
      def fun(arr, tar):
        l, r = 0, len(arr) -1
        while l <= r:
          m = l + (r - l) // 2
          if arr[m] == tar:
            return True 
          elif arr[m] < tar:
            l = m + 1
          else:
            r = m - 1 
        return False
      
      #main code
      # u --> up, d --> down
      u, d = 0, len(mat) -1 
      while u <= d:
        mid = u + (d - u) // 2 
        if mat[mid][0] <= target <= mat[mid][-1]:
          return fun(mat[mid], target)
        elif mat[mid][0] < target:
          u = mid + 1 
        else:
          d = mid - 1
      return False

