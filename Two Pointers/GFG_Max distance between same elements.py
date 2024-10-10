
'''
Given an array arr[] with repeated elements, the task is to find the maximum distance between two occurrences of an element.

Note: You may assume that every input array has repetitions.

Examples:

Input: arr = [1, 1, 2, 2, 2, 1]
Output: 5
Explanation: distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, So max distance is 5.
Input: arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Output: 10
Explanation: maximum distance for 2 is 11-1 = 10, maximum distance for 1 is 4-2 = 2 ,maximum distance for 4 is 10-5 = 5, So max distance is 10.
Expected Time Complexity :  O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 <= arr.size() <= 106
1 <= arr[i] <= 109
'''
#Brute Force:
class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if arr[i] == arr[j]:
                    res = max(res, j - i)
                    break 
        return res 

#Optimal
class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        
        n = len(arr)
        res = 0
        mapp = {}
        for i in range(n-1, -1, -1):
            if arr[i] not in mapp:
                mapp[arr[i]] = i 
        
        for i in range(n):
            res = max(res, mapp[arr[i]] - i)
        return res 


#LC_962. Maximum Width Ramp
'''
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

Constraints:

2 <= nums.length <= 5 * 104
0 <= nums[i] <= 5 * 104
'''
#Brute Force:
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] <= nums[j]:
                    res = max(res, j - i)
        return res 
        
#Optimal:
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        n = len(nums)
        next_max = [-1] * n 
        next_max[n - 1] = nums[-1]
        for i in range(n - 2, -1, -1):
            next_max[i] = max(nums[i], next_max[i + 1])

        res = 0 
        i, j = 0, 0 
        while i < n and j < n:
            if nums[i] <= next_max[j]:
                res = max(res, j - i)
                j += 1
            else:
                i += 1
        return res 

        
        

