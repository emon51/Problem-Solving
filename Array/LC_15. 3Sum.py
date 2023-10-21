class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        
        for i in range(n):
            l, r = i+1, n - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif sm < 0:
                    l += 1
                else:
                    r -= 1
                    
        return res
        
