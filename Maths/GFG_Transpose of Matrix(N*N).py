class Solution:
    def transpose(self, mat, n):
        for r in range(n):
            for c in range(r, n):
                mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
                
        return mat
