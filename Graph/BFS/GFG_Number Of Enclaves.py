#Solution_01
from typing import List
from collections import deque
class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        
        def _valid(r, c, m, n):
            return r >= 0 and r < m and c >= 0 and c < n
            
        def bfs(grid, r, c, m, n):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            cnt = 0
            while q:
                r, c = q.popleft()
                cnt += 1
                for i, j in dirs:
                    dr, dc = r + i, c + j
                    if _valid(dr, dc, m, n) and grid[dr][dc]:
                        q.append((dr, dc))
                        grid[dr][dc] = 0
            return cnt
                        
        
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        #For first row
        for c in range(n):
            if grid[0][c]:
                bfs(grid, 0, c, m, n)
                
        #For last row
        for c in range(n):
            if grid[m - 1][c]:
                bfs(grid, m - 1, c, m, n)
                
        #For first column
        for r in range(m):
            if grid[r][0]:
                bfs(grid, r, 0, m, n)
        
        #For last column
        for r in range(m):
            if grid[r][n - 1]:
                bfs(grid, r, n - 1, m, n)
                
        #Checking for Enclaves inside the boundary
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    res += bfs(grid, r, c, m, n)
        return res



#Solution_02
#User function Template for python3

from typing import List
from collections import deque
class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        
        def _valid(r, c, m, n):
            return r >= 0 and r < m and c >= 0 and c < n
            
        def bfs(grid, r, c, m, n):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            cnt = 0
            while q:
                r, c = q.popleft()
                cnt += 1
                for i, j in dirs:
                    dr, dc = r + i, c + j
                    if _valid(dr, dc, m, n) and grid[dr][dc]:
                        q.append((dr, dc))
                        grid[dr][dc] = 0
            return cnt
                        
        
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        #Checking boundary
        for r in range(m):
            for c in range(n):
                if grid[r][c] and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                    bfs(grid, r, c, m, n)
                    
        #Checking for Enclaves inside the boundary
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    res += bfs(grid, r, c, m, n)
        return res
                
        
                
                
                
                
                
