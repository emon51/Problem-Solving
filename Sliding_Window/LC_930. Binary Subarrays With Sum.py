#01
class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        
        n = len(nums); sumAtMostK = 0; sumAtMostK_1 = 0
        
        
        csm = 0; l = 0
        for r in range(n):
            csm += nums[r]
            while l <= r and csm > k:
                csm -= nums[l]
                l += 1
            sumAtMostK += (r - l + 1)
            
        csm = 0; l = 0
        for r in range(n):
            csm += nums[r]
            while l <= r and csm > (k - 1):
                csm -= nums[l]
                l += 1
            sumAtMostK_1 += (r - l + 1)
        
        return sumAtMostK - sumAtMostK_1

#02
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        n = len(nums);        
        
        def fun(k):
            csm = 0; l = 0; res = 0
            for r in range(n):
                csm += nums[r]
                while l <= r and csm > k:
                    csm -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res
        
        return fun(goal) - fun(goal - 1)

#03
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        n = len(nums); d = {}; csm = 0; res = 0
        
        for r in range(n):
            d[csm] = d.get(csm, 0) + 1
            csm += nums[r]
            if (csm - goal) in d:
                res += d[csm - goal]
        return res












