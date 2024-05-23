class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:


        def fun(r, c, i, vis):
            if i == len(word):
                return True 
            
            vis.add((r, c))
            res = False
            for x, y in dirs:
                dr, dc = r + x, c + y 
                if (0 <= dr < m and 0 <= dc < n) and (dr, dc) not in vis and grid[dr][dc] == word[i]:
                    res = res or fun(dr, dc, i + 1, vis)
            vis.remove((r, c))
            return res



        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == word[0]:
                    res = fun(r, c, 1, set())
                    if res:
                        return True
        return False

        
