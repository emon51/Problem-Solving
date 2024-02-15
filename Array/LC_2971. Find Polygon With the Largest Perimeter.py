
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        #Prefix sum
        n = len(nums)
        prefixSum = [-1] * n
        prefixSum[0] = nums[0]
        for i in range(1, n):
            prefixSum[i] = nums[i] + prefixSum[i - 1]
        #print(prefixSum)
        perimeter = -1
        for i in range(2, n):
            if prefixSum[i - 1] > nums[i]:
                perimeter = prefixSum[i - 1] + nums[i]
        
        return perimeter
