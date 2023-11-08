import heapq
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        
        def __valid(x, y):
            return x >= 0 and x < m and y >= 0 and y < n
        
        r = 0 
        for c in range(n):
            x, y = r, c 
            heap = []
            while __valid(x, y):
                heapq.heappush(heap, mat[x][y])
                x += 1
                y += 1
                
            x, y = r, c
            while heap:
                val = heapq.heappop(heap)
                mat[x][y] = val
                x += 1
                y += 1
                
        
        c = 0
        for r in range(1, m):
            x, y = r, c 
            heap = []
            while __valid(x, y):
                heapq.heappush(heap, mat[x][y])
                x += 1
                y += 1
                
            x, y = r, c
            while heap:
                val = heapq.heappop(heap)
                mat[x][y] = val
                x += 1
                y += 1
                
        return mat
                
        
                
                
                
                
                
                
                
                
                
