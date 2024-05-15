'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

#Brute Force
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        res = 0 
        for i in range(n):
            zerocnt = 0
            onecnt = 0
            curr = 0
            for j in range(i, n):
                zerocnt += 1 if nums[j] == 0 else 0
                onecnt += 1 if nums[j] == 1 else 0
                if zerocnt <= 1:
                    curr = max(curr, onecnt)
                else:
                    break
            if zerocnt == 0:
                curr -= 1
            res = max(curr, res)

        return res
        

#Sliding Window_1
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        res = 0 
        zerocnt, onecnt = 0, 0
        l = 0 
        gotZero = False
        for r, num in enumerate(nums):
            if num == 1:
                onecnt += 1
            else:
                gotZero = True
                zerocnt += 1
            
            while zerocnt > 1:
                if nums[l] == 1:
                    onecnt -= 1
                else:
                    zerocnt -= 1
                l += 1
            res = max(res, onecnt)

        return res if gotZero else res - 1
            

#Sliding Window_2
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        res = 0 
        zerocnt = 0
        l = 0 
        for r, num in enumerate(nums):
            zerocnt += 1 if num == 0 else 0
            while zerocnt > 1:
                zerocnt -= 1 if nums[l] == 0 else 0
                l += 1
            res = max(res, r - l) #substring_length - deleted_num --> (r - l + 1 - 1) = (r - l)
        return res
            

        
