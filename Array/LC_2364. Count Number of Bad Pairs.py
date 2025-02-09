
'''
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

 

Example 1:

Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
'''

#Brute Force 
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        n, res = len(nums), 0 
        for i in range(n):
            for j in range(i + 1, n):
                res += 1 if (j - i) != (nums[j] - nums[i]) else 0 
        return res 
        

#Optimal 
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        def  fact(n):
            fct = 1
            for num in range(2, n + 1):
                fct *= num 
            return fct 
            
        def ncr(n, r):
            return fact(n) // (fact(n - r) * fact(r))
        n = len(nums)
        res = 0 
        #good_pair:  nums[i] - i == nums[j] - j 
        mapp = {}
        for i, num in enumerate(nums):
            mapp[(num - i)] = mapp.get((num - i), 0) + 1 
        
        good_pair = 0 
        for key, val in mapp.items():
            good_pair += ncr(val, 2)
        
        total_pair = (n * (n - 1)) // 2 

        bad_pair = total_pair - good_pair 

        return bad_pair 


        
