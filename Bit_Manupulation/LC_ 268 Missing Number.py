class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        return n*(n+1)//2 - sum(nums)

#===================================================================#

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        res = 0

        for num in nums:
            res ^= num

        for num in range(n+1):
            res ^= num

        return res
