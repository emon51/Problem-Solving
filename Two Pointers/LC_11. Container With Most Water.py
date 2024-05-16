'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''



#Brute force, TC: O(N^2), SC: O(1)
class Solution:
    def maxArea(self, nums: List[int]) -> int:

        res = 0
        n = len(nums)

        for i in range(n):
            left = 0
            l = i - 1
            while l >= 0:
                left = max(left, min(nums[i], nums[l]) * (i - l))
                l -= 1
            right = 0
            r = i + 1
            while r < n:
                right = max(right, min(nums[i], nums[r]) * (r - i))
                r += 1

            res = max(res, left, right)
        return res        


#Brute force, TC: O(N^2), SC: O(1)
class Solution:
    def maxArea(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                res = max(res, min(nums[i], nums[j]) * (j - i))
        return res
        


#Optimal, TC: O(N), SC: O(1)
class Solution:
    def maxArea(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        l, r = 0, n -1
        while l < r:
            curr = min(nums[l], nums[r]) * (r - l)
            res = max(res, curr)
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
        return res
                
