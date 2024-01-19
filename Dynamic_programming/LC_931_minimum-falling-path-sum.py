"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element in the next row that 
is either directly below or diagonally left/right. Specifically, 
the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
"""
#TLE
class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:

        def valid(r, c, n):
            return r >= 0 and r < n and c >= 0 and c < n
        
        def dfs(mat, r, c, n):
            if not valid(r, c, n):
                return float('inf')
            if r == (n-1):
                return mat[r][c]
            
            p1 = mat[r][c] + dfs(mat, r + 1, c, n)
            p2 = mat[r][c] + dfs(mat, r + 1, c - 1, n)
            p3 = mat[r][c] + dfs(mat, r + 1, c + 1, n)
            return min(p1, p2, p3)

        res = float('inf')
        n = len(mat)
        for c in range(n):
            res = min(res, dfs(mat, 0, c, n))
        return res
      

#Accepted
class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:

        def valid(r, c, n):
            return r >= 0 and r < n and c >= 0 and c < n
        
        def dfs(mat, r, c, n):
            if not valid(r, c, n):
                return float('inf')
            if (r, c) in dp:
                return dp[(r, c)]
            if r == (n-1):
                return mat[r][c]
            
            p1 = mat[r][c] + dfs(mat, r + 1, c, n)
            p2 = mat[r][c] + dfs(mat, r + 1, c - 1, n)
            p3 = mat[r][c] + dfs(mat, r + 1, c + 1, n)
            val = min(p1, p2, p3)
            dp[(r, c)] = val
            return val

        res = float('inf')
        n = len(mat)
        dp = {}
        for c in range(n):
            res = min(res, dfs(mat, 0, c, n))
        return res



