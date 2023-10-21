
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
                
