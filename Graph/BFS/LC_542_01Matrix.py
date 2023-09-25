#Leetcode: 542_01 Matrix
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
      
      m, n = len(mat), len(mat[0])
      q = deque()
      vis = set()
      dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)] 
    
      def _valid(r, c):
        return r >= 0 and c >= 0 and r < m and c < n
      
      #multi source 
      for r in range(m):
        for c in range(n):
          if mat[r][c] == 0:
            q.append((r, c, 0))
            vis.add((r, c))
        
      while q:
        r, c, d = q.popleft()
        for i, j in dirs:
          dr, dc = r + i, c + j 
          if _valid(dr, dc) and (dr, dc) not in vis:
            mat[dr][dc] = d + 1 
            q.append((dr, dc, d + 1))
            vis.add((dr, dc))
              
      
      return mat
             