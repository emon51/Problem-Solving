class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        dr = {i: set() for i in range(9)}
        dc = {i: set() for i in range(9)}
        dsq = {(i, j): set() for j in range(3) for i in range(3)}
      
   
        
        for r in range(9):
            for c in range(9): 
                val = board[r][c]
                if val == '.':
                    continue
                if val in dr[r] or val in dc[c] or val in dsq[(r//3, c//3)]:
                    return False
                dr[r].add(val)
                dc[c].add(val)
                dsq[(r//3, c//3)].add(val)
      
        return True
                
               
                        
                        
                        
