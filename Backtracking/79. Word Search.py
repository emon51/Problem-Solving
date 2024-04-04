
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def _valid(r, c):
            return r >= 0 and r < m and c >= 0 and c < n

        def dfs(r, c, i, vis):
            if i == len(word):
                return True 
            for x, y in dirs:
                dr, dc = r + x, c + y
                if _valid(dr, dc) and (dr, dc) not in vis and board[dr][dc] == word[i]:
                    vis.add((dr, dc))
                    if dfs(dr, dc, i + 1, vis):
                        return True
                    vis.remove((dr, dc))  # Backtrack

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 1, {(r, c)}):
                    return True
        return False
