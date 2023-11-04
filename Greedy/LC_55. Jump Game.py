#DP_TLE
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def fun(i, memo = {}):
            if i in memo:
                return memo[i]
            if i == (N - 1):
                return True
            if i >= N:
                return False
            res = False
            for j in range(1, nums[i] +1):
                res = res or fun(i+j)
            memo[i] = res
            return res
            
        N = len(nums)
        return fun(0)

  #==============================================================================#

#Greedy(Accepted) TC: O(N)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n-1, -1, -1):
            if (i + nums[i]) >= goal:
                goal = i
        
        return goal == 0
