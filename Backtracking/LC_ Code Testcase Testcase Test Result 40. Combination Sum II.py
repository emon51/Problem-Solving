
'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''


from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        
        def fun(arr, i, n, target, p = []):
            if target == 0:
                res.append(p)
                return
            if i == n or target < 0:
                return
            # Explore with current element
            fun(arr, i + 1, n, target - arr[i], p + [arr[i]])
            # Skip duplicates
            j = i + 1
            while j < n and arr[j] == arr[i]:
                j += 1
            # Explore without current element
            fun(arr, j, n, target, p)
        
        candidates.sort()
        fun(candidates, 0, len(candidates), target)

        return res
