
'''
Given a square grid of size N, each cell of which contains an integer cost that represents a cost to traverse through that cell, we need to find a path from the top left cell to the bottom right cell by which the total cost incurred is minimum.
From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j).  

Examples :

Input: grid = {{9,4,9,9},{6,7,6,4},{8,3,3,7},{7,4,9,10}}
Output: 43
Explanation: The grid is-
9 4 9 9
6 7 6 4
8 3 3 7
7 4 9 10
The minimum cost is-
9 + 4 + 7 + 3 + 3 + 7 + 10 = 43.
Input: grid = {{4,4},{3,7}}
Output: 14
Explanation: The grid is-
4 4
3 7
The minimum cost is- 4 + 3 + 7 = 14.
Expected Time Complexity: O(n2*log(n))
Expected Auxiliary Space: O(n2) 
 Constraints:
1 ≤ n ≤ 500
1 ≤ cost of cells ≤ 500


'''



import heapq 
class Solution:
    
    #Function to return the minimum cost to react at bottom
    #right cell from top left cell.
    def minimumCostPath(self, grid):
        
        m, n = len(grid), len(grid[0])
        dist = [[float('inf') for _ in range(n)] for _ in range(m)] 
        dist[0][0] = grid[0][0]
        heap = [(grid[0][0], 0, 0)] #wt, row, col
        
        while heap:
            d, r, c = heapq.heappop(heap)
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dr, dc = r + x, c + y 
                if not ((0 <= dr < m) and (0 <= dc < n)): 
                    continue 
                if (grid[dr][dc] + d) < dist[dr][dc]:
                    dist[dr][dc] = grid[dr][dc] + d  
                    heapq.heappush(heap, (dist[dr][dc], dr, dc))
        return dist[m - 1][n - 1]
                





















