#Leetcode: 994_Rotten_Oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
      
      M, N = len(grid), len(grid[0]) 
      q = deque()
      fresh = 0 
      
      dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
      
      def __valid(r, c):
        return r >= 0 and c >= 0 and r < M and c < N
      
      for r in range(M):
        for c in range(N):
          if grid[r][c] == 1:
            fresh += 1 
          if grid[r][c] == 2:
            q.append((r, c, 0))
      
      if fresh == 0:
        return 0 
      
      while q:
        r, c, t = q.popleft()
        for i, j in dirs:
          dr, dc = r + i, c + j 
          if __valid(dr, dc) and grid[dr][dc] == 1:
            grid[dr][dc] = 2 
            fresh -= 1
            q.append((dr, dc, t + 1))
            
      if fresh:
        return -1 
      
      return t
            