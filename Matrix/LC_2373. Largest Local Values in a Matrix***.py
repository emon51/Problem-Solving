
#Brute Force(Accepted)
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        res = [[-1] * (n - 2) for _ in range(n - 2)]

        for r in range(n - 2):
            for c in range(n - 2):
                curr = grid[r][c]
                for i in range(r, 3 + r):
                    for j in range(c, 3 + c):
                        curr = max(curr, grid[i][j])
                res[r][c] = curr
        return res
