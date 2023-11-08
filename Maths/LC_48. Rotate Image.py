class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        for r in range(n):
            for c in range(r, n):
                mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
        
        for r in range(n):
            mat[r] = mat[r][::-1]
            
        #return mat
