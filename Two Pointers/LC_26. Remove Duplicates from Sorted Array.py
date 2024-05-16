
'''
Problem statement
You are given a sorted integer array 'arr' of size 'n'.

You need to remove the duplicates from the array such that each element appears only once.

Return the length of this new array.

Note:
Do not allocate extra space for another array. You need to do this by modifying the given input array in place with O(1) extra memory. 


For example:
'n' = 5, 'arr' = [1 2 2 2 3].
The new array will be [1 2 3].
So our answer is 3.
'''


#Brute Force
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return len(set(nums))


#Optimal
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 1

        while r < n:
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1
    

        
