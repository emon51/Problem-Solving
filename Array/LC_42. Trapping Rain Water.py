class Solution:
    def trap(self, nums: List[int]) -> int:
        
        n = len(nums)
        LH, RH = [], []
        prev = -1
        for h in nums:
            LH.append(max(prev, h))
            prev = max(prev, h)
        prev = -1   
        for h in nums[::-1]:
            RH.append(max(prev, h))
            prev  = max(prev, h)
        RH = RH[::-1]
        
        res = 0
        for i in range(1, n-1):
            water = min(LH[i-1], RH[i+1]) - nums[i]
            res += water if water > 0 else 0
        return res
        
