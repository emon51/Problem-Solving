#Leetcode: 695_Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      
      m, n = len(grid), len(grid[0])
      dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
      vis = set()
      
      def _valid(r, c):
        return r >= 0 and c >= 0 and r < m and c < n
      
      def bfs(sr, sc):
        q = deque() 
        q.append((sr, sc))
        vis.add((sr, sc)) 
        
        area = 0 
        
        while q: 
          r, c = q.popleft()
          area += 1
          for i, j in dirs:
            dr, dc = r + i, c + j 
            if _valid(dr, dc) and grid[dr][dc] and (dr, dc) not in vis:
              q.append((dr, dc)) 
              vis.add((dr, dc)) 
        return area
      
      res = 0
      for r in range(m):
        for c in range(n):
          if grid[r][c] and (r, c) not in vis:
            res = max(res, bfs(r, c))
      return res
        