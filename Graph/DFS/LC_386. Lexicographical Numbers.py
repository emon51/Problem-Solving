
'''
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104

'''

#Simple DFS
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        def dfs(num):
            nonlocal res
            res.append(num)
            for i in range(10):
                new = num * 10 + i 
                if new <= n:
                    dfs(new)
        
        res = []
        for num in range(1, 10):
            if num <= n:
                dfs(num)
        return res

        