class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = [-1] * n
        right_min = [-1] * n

        curr_max = float('-inf')
        for i, num in enumerate(nums):
            curr_max = max(curr_max, num)
            left_max[i] = curr_max
        
        curr_min = float("inf")
        for i in range(n - 1, - 1, - 1):
            curr_min = min(curr_min, nums[i])
            right_min[i] = curr_min

        for i in range(n - 1):
            if left_max[i] <= right_min[i + 1]:
                return i + 1

        
