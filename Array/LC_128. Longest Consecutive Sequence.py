class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums)) #removed duplicates
        nums.sort()
        res = 0 
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        cnt = 1
        for i in range(1, n):
            if nums[i] -1 == nums[i-1]:
                cnt += 1
            else:
                cnt = 1
                    
            res = max(res, cnt)
        return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = 0 
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        cnt = 1
        for i in range(1, n):
            if nums[i] -1 == nums[i-1]:
                cnt += 1
            elif nums[i] != nums[i-1]:
                cnt = 1
            res = max(res, cnt)
        return res

