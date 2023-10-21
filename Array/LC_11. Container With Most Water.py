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
                
