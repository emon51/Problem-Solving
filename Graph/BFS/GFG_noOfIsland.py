"""
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.

Note: An island is either surrounded by water or boundary of grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Example 1:

Input:
grid = {{0,1},{1,0},{1,1},{1,0}}
Output:
1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.
Example 2:

Input:
grid = {{0,1,1,1,0,0,0},{0,0,1,1,0,1,0}}
Output:
2
Expanation:
The grid is-
0 1 1 1 0 0 0
0 0 1 1 0 1 0 
There are two islands :- one is colored in blue 
and other in orange.
Your Task:
You don't need to read or print anything. Your task is to complete the function numIslands() which takes the grid as an input parameter and returns the total number of islands.

Expected Time Complexity: O(n*m)
Expected Space Complexity: O(n*m)

Constraints:
1 ≤ n, m ≤ 500
"""

#BFS
#User function Template for python3

import sys
sys.setrecursionlimit(10**8)

from collections import deque

class Solution:
    def numIslands(self,grid):
        
       m, n = len(grid), len(grid[0])
       vis = [[0 for _ in range(n)] for _ in range(m)] 
       
       def _valid(r, c):
           return r >= 0 and c >= 0 and r < m and c < n
           
       def bfs(r, c):
           q = deque()
           q.append((r, c))
           vis[r][c] = 1
           dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
           
           while q:
               r, c = q.popleft()
               for i, j in dirs:
                   dr, dc = r + i, c + j 
                   if _valid(dr, dc) and grid[dr][dc] and not vis[dr][dc]:
                       q.append((dr, dc))
                       vis[dr][dc] = 1
           return 1 
            
       res = 0 
       for r in range(m):
           for c in range(n):
               if grid[r][c] and not vis[r][c]:
                    res += bfs(r, c)
       return res
               
           
           