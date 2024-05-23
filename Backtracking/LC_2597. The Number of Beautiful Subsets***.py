
'''
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. 
Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].
 

Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000

'''

#TLE
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        all_subset = []
        n = len(nums)

        def beautiful(arr, k):
            if not arr:
                return False
            lenn = len(arr)
            for i in range(lenn):
                for j in range(i + 1, lenn):
                    if abs(arr[i] - arr[j]) == k:
                        return False
            return True 

        def fun(i, p = []):    
            nonlocal all_subset, n
            if i == n:
                all_subset.append(p)
                return 
            fun(i + 1, p + [nums[i]])
            fun(i + 1, p)

        fun(0)
        res = 0
        for subset in all_subset:
            res += 1 if beautiful(subset, k) else 0
        return res   


#Accepted
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        res = 0
        n = len(nums)
        mapp = defaultdict(int)

        def beautiful(mapp, k, num):
            if mapp[num - k] == 0 and mapp[num + k] == 0:
                return True 
            return False

        def fun(i):    
            nonlocal res
            if i == n:
                res += 1
                return 
            if beautiful(mapp, k, nums[i]):
                mapp[nums[i]] += 1
                fun(i + 1)
                mapp[nums[i]] -= 1 #Backtrack
            fun(i + 1)

        fun(0)
        return res - 1 # -1 for empty subset


#Accepted 
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        n = len(nums)

        def beautiful(mapp, num):
            if mapp[num - k] == 0 and mapp[num + k] == 0:
                return True 
            return False

        mapp = defaultdict(lambda: 0)
        def fun(i):    
            nonlocal mapp
            if i == n:
                return 1 
            pick = 0
            if beautiful(mapp, nums[i]):
                mapp[nums[i]] += 1
                pick = fun(i + 1)
                mapp[nums[i]] -= 1
            notpick = fun(i + 1)
            return pick + notpick

        return fun(0) - 1
        
