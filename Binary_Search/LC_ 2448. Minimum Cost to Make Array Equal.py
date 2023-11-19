class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        #helper function
        def _cost(mid):
            cst = 0
            for i, num in enumerate(nums):
                cst += (abs(num - mid) * cost[i])
            return cst
        
        res = float('inf')
        l, r = min(nums), max(nums)
        while l <= r:
            mid = l + (r - l) // 2
            mid_cost1 = _cost(mid)
            mid_cost2 = _cost(mid+1)
            if mid_cost1 < mid_cost2:
                res = min(res, mid_cost1)
                r = mid - 1
            else:
                l = mid + 1
        return res
                
        
