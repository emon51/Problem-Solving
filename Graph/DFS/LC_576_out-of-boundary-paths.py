
#BFS(MLE)
from collections import deque

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        def valid(r, c):
            return r >= 0 and r < m and c >= 0 and c < n

        q = deque()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q.append((startRow, startColumn, maxMove))
        res = 0

        while q:
            r, c, rem_move = q.popleft()

            if not valid(r, c):
                res += 1
            elif rem_move > 0:
                for i, j in dirs:
                    dr, dc = r + i, c + j
                    q.append((dr, dc, rem_move - 1))
            
        return res % (10**9 + 7)

#DFS(Accepted)
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        memo = {}

        def dfs(row, col, moves):
            # Check if the ball is out of bounds
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1

            # Check if maxMove is exhausted
            if moves == 0:
                return 0

            # Check if the result is already memoized
            if (row, col, moves) in memo:
                return memo[(row, col, moves)]

            # Explore all possible moves
            paths = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                paths += dfs(new_row, new_col, moves - 1)
                paths %= MOD

            # Memoize the result
            memo[(row, col, moves)] = paths

            return paths

        # Start DFS from the initial position
        result = dfs(startRow, startColumn, maxMove)
        return result % MOD



  
