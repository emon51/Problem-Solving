#GFG: Shortest Distance in a Binary Maze

#User function Template for python3
from collections import deque 
from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        #BFS 
        m, n = len(grid), len(grid[0])
        q = deque() 
        q.append((source[0], source[1], 0))
        
        vis = set()
        vis.add(tuple(source))
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def _valid(r, c):
            return r >= 0 and c >= 0 and r < m and c < n
            
        while q:
            r, c, w = q.popleft() 
            if r == destination[0] and c == destination[1]:
                return w
            for i, j in dirs:
                dr, dc = r + i, c + j 
                if _valid(dr, dc) and (dr, dc) not in vis and grid[dr][dc]:
                    q.append((dr, dc, w + 1)) 
                    vis.add((dr, dc)) 
        return -1