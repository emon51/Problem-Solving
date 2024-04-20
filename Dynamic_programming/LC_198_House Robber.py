
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

#TLE
class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(arr, i, n):
            if i >= n:
                return 0
            pick = arr[i] + dfs(arr, i + 2, n)
            notPick = dfs(arr, i + 1, n)
            return max(pick, notPick)

        return dfs(nums, 0, len(nums))
        

#Accepted
class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(arr, i, n, dp = {}):
            if i in dp:
                return dp[i]
            if i >= n:
                return 0
            pick = arr[i] + dfs(arr, i + 2, n, dp)
            notPick = dfs(arr, i + 1, n, dp)
            val = max(pick, notPick)
            dp[i] = val
            return val
        return dfs(nums, 0, len(nums))

#Tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        for i in range(1, n):
            f1 = nums[i]
            if (i - 2) >= 0:
                f1 += dp[i - 2]
            f2 = 0 + dp[i - 1]
            val = max(f1, f2)
            dp[i] = val 

        return dp[n - 1]

#Tabulation + Space Optimizaton O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        prev1 = nums[0]
        prev2 = 0
        for i in range(1, n):
            f1 = nums[i] + prev2
            f2 = 0 + prev1
            val = max(f1, f2)
            prev2 = prev1
            prev1 = val 

        return prev1

        
