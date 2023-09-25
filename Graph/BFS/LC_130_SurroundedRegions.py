#Leetcode: 130_Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        q = deque()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        vis = set()
        #multi source
        
        #checking 1st row 
        r = 0 
        for c in range(n):
          if board[r][c] == "O":
            q.append((r, c))
            vis.add((r, c))
            
        #checking last row 
        r = m - 1 
        for c in range(n):
          if board[r][c] == "O":
            q.append((r, c))
            vis.add((r, c))
            
        #checking 1st column 
        c = 0 
        for r in range(m):
          if board[r][c] == "O":
            q.append((r, c))
            vis.add((r, c))
        
        #checking last column 
        c = n - 1 
        for r in range(m):
          if board[r][c] == "O":
            q.append((r, c))
            vis.add((r, c))
       
        def _valid(r, c):
          return r >= 0 and c >= 0 and r < m and c < n 
        
        while q:
          r, c = q.popleft()
          board[r][c] = 0 
          for i, j in dirs:
            dr, dc = r + i, c + j 
            if _valid(dr, dc) and board[dr][dc] == "O" and (dr, dc) not in vis:
              q.append((dr, dc))
              vis.add((dr, dc))
                   
        #print(board)    
        for r in range(m):
          for c in range(n):
            if board[r][c] == "O":
              board[r][c] = "X"
            if board[r][c] == 0:
              board[r][c] = "O"
              
####OR####

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        q = deque()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        vis = set()
        #multi source
        """
        #checking 1st row 
        r = 0 
        for c in range(n):
          if board[r][c] == "O":
            q.append((r, c))
            vis.add((r, c))
            
        #checking last row 
        r = m - 1 
        for c in range(n):
          if board[r][c] == "O":
            q.append((r, c))
            vis.add((r, c))
            
        #checking 1st column 
        c = 0 
        for r in range(m):
          if board[r][c] == "O":
            q.append((r, c))
            vis.add((r, c))
        
        #checking last column 
        c = n - 1 
        for r in range(m):
          if board[r][c] == "O":
            q.append((r, c))
            vis.add((r, c))
        """
        for r in range(m):
          for c in range(n):
            if r == 0 or c == 0 or r == m -1 or c == n -1:
              if board[r][c] == "O":
                q.append((r, c))
                vis.add((r, c))
       
        def _valid(r, c):
          return r >= 0 and c >= 0 and r < m and c < n 
        
        while q:
          r, c = q.popleft()
          board[r][c] = 0 
          for i, j in dirs:
            dr, dc = r + i, c + j 
            if _valid(dr, dc) and board[dr][dc] == "O" and (dr, dc) not in vis:
              q.append((dr, dc))
              vis.add((dr, dc))
                   
        #print(board)    
        for r in range(m):
          for c in range(n):
            if board[r][c] == "O":
              board[r][c] = "X"
            if board[r][c] == 0:
              board[r][c] = "O"