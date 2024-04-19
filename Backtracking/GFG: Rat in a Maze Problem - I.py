'''
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.
Example 2:
Input:
N = 2
m[][] = {{1, 0},
         {1, 0}}
Output:
-1
Explanation:
No path exists and destination cell is 
blocked.
Your Task:  
You don't need to read input or print anything. Complete the function printPath() which takes N and 2D array m[ ][ ] as input parameters and returns the list of paths in lexicographically increasing order. 
Note: In case of no path, return an empty list. The driver will output "-1" automatically.

Expected Time Complexity: O((3N^2)).
Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths.

Constraints:
2 ≤ N ≤ 5
0 ≤ m[i][j] ≤ 1


'''

#User function Template for python3
class Solution:
  def findPath(self, mat, n):
    dirs = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
    res = []
    visited = set()

    def valid(r, c):
      return 0 <= r and r < n and 0 <= c and c < n

    def dfs(r, c, p=''):
      if r == n - 1 and c == n - 1:
        res.append(p)
        return
      for x, y, d in dirs:
        if valid(r + x, c + y) and mat[r + x][c + y] and (r + x, c + y) not in visited:
          visited.add((r, c))  # Add current cell to visited set
          dfs(r + x, c + y, p + d)
          visited.remove((r, c))  # Remove current cell after exploring that path
          
    if mat[0][0] != 1:
        return [-1]
    dfs(0, 0)
    return res

#=====================================================================================#
class Solution:
  def findPath(self, mat, n):
    dirs = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
    res = []
    
    def valid(r, c):
      return 0 <= r < n and 0 <= c < n

    def dfs(r, c, p=''):
      if r == n - 1 and c == n - 1:
        res.append(p)
        return
      for x, y, d in dirs:
          dr, dc = r + x, c + y
          if valid(dr, dc) and mat[dr][dc]:
              mat[r][c] = 0  # Add current cell to visited set
              dfs(r + x, c + y, p + d)
              mat[r][c] = 1  # Remove current cell after exploring that path
          
          
    if mat[0][0] == 0:
        return [-1]
    dfs(0, 0)
    return res if res else [-1]
