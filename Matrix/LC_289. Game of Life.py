
import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

        m, n = len(board), len(board[0])

        copy_board = copy.deepcopy(board)
        #print(copy_board)
        for r in range(m):
            for c in range(n):
                live = 0
                for i, j in dirs:
                    dr, dc = r + i, c + j
                    if (dr >= 0 and dr < m and dc >= 0 and dc < n) and copy_board[dr][dc] == 1:
                        live += 1
                if copy_board[r][c] == 1 and (live < 2 or live > 3):
                    board[r][c] = 0
                elif copy_board[r][c] == 0 and live == 3:
                    board[r][c] = 1
                    
          
               
                

        
