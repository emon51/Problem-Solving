#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)

from collections import deque 
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        res_set = set() 
        dirs = [(1, 0), (0, 1), (-1,0), (0, -1)]
        vis = set()
        
        def _valid(r, c):
            return r >= 0 and c >= 0 and r < m and c < n
        
        def bfs(r, c, sr, sc):
            res = [] 
            q = deque() 
            q.append((r, c))
            vis.add((r, c)) 
            
            while q:
                r, c = q.popleft()
                res.append((r - sr, c - sc))
                
                for i, j in dirs:
                    dr, dc = r + i, c + j 
                    
                    if _valid(dr, dc) and grid[dr][dc] and (dr, dc) not in vis:
                        q.append((dr, dc)) 
                        vis.add((dr, dc))
            
            res_set.add(tuple(res))
            
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] and (r, c) not in vis:
                    bfs(r, c, r, c)
                    
        return len(res_set)