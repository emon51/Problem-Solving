
'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
 

Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?


'''
#TLE
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        res = 0
        def fun(tar):
            nonlocal res
            if tar == 0:
                res += 1
                return
            if tar < 0:
                return 
            for nm in nums:
                fun(tar - nm)

        fun(target)
        return res
        
#TLE
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        def fun(tar):
            if tar == 0:
                return 1
            if tar < 0:
                return 0
            count = 0
            for nm in nums:
                count += fun(tar - nm)
            return count

        return fun(target)
        

#Memoization
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        def fun(tar, dp = {}):
            if tar in dp:
                return dp[tar]
            if tar == 0:
                return 1
            if tar < 0:
                return 0
            count = 0
            for nm in nums:
                count += fun(tar - nm, dp)
            dp[tar] = count
            return count

        return fun(target)
        
