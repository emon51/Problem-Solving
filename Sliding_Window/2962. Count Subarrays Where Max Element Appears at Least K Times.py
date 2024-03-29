
'''
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
'''

#Brute-Force

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums); res = 0; max_value = max(nums)
        for i in range(n):
            mapp = {}
            for j in range(i, n):
                mapp[nums[j]] = mapp.get(nums[j], 0) + 1
                if mapp.get(max_value, 0) >= k:
                    res += 1
        
        return res

#Accepted

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        res = 0
        max_val = max(nums)
        mapp = {}
        l = 0

        for r in range(n):
            mapp[nums[r]] = mapp.get(nums[r], 0) + 1
            while l <= r and mapp.get(max_val, 0) >= k:
                res += (n - r)
                mapp[nums[l]] -= 1
                l += 1
        
        return res
        



