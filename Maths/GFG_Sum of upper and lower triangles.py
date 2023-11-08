class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self, mat, n):
        up_sum = 0
        low_sum = 0
        for r in range(n):
            for c in range(r, n):
                up_sum += mat[r][c]
        
        for r in range(n):
            for c in range(r + 1):
                low_sum += mat[r][c]
                
        return [up_sum, low_sum]
        
