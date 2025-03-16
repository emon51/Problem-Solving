
'''
Given an array arr[] of size n, where arr[i] denotes the height of ith stone. Geek starts from stone 0 and from stone i, he can jump to stones i + 1, i + 2, … i + k. The cost for jumping from stone i to stone j is abs(arr[i] – arr[j]). Find the minimum cost for Geek to reach the last stone.

Example:

Input: k = 3, arr[]= [10, 30, 40, 50, 20]
Output: 30
Explanation: Geek will follow the path 1->2->5, the total cost would be |10-30| + |30-20| = 30, which is minimum.
Input: k = 1, arr[]= [10, 20, 10]
Output: 20
Explanation: Geek will follow the path 1->2->3, the total cost would be |10 - 20| + |20 - 10| = 20.
Constraints:

1 <= arr.size() <=104
1 <= k <= 100
1 <= arr[i] <= 104

'''

#DFS 
class Solution:
    def minimizeCost(self, k, arr):
        
        def dfs(n):
            if n == 0:
                return 0 
            if n < 0:
                return float('inf')
            res = float('inf')
            for i in range(1, k + 1):
                if (n - i) >= 0:
                    curr = abs(arr[n] - arr[n - i]) + dfs(n - i)
                    res = min(res, curr)
            return res 
        
        return dfs(len(arr) - 1)
        
                


#DFS + Memoization 
class Solution:
    def minimizeCost(self, k, arr):
        
        def dfs(n, dp):
            if n in dp:
                return dp[n]
            if n == 0:
                return 0 
            if n < 0:
                return float('inf')
            res = float('inf')
            for i in range(1, k + 1):
                if (n - i) >= 0:
                    curr = abs(arr[n] - arr[n - i]) + dfs(n - i, dp)
                    res = min(res, curr)
            dp[n] = res 
            return res 
        
        return dfs(len(arr) - 1, {})
        
                


#Tabulation 
class Solution:
    def minimizeCost(self, k, arr):
        
        n = len(arr)
        dp = [0] * n 
        for i in range(1, n):
            curr = float('inf')
            for j in range(1, k + 1):
                if (i - j) >= 0:
                    curr = min(abs(arr[i] - arr[i - j]) + dp[i - j], curr)
            dp[i] = curr 
        
        return dp[n - 1]
        
