"""
#GFG:Shortest Source to Destination Path
Given a 2D binary matrix A(0-based index) of dimensions NxM. Find the minimum number of steps required to reach from (0,0) to (X, Y).
Note: You can only move left, right, up and down, and only through cells that contain 1.

Example 1:

Input:
N=3, M=4
A=[[1,0,0,0], 
   [1,1,0,1],
   [0,1,1,1]]
X=2, Y=3 
Output:
5
Explanation:
The shortest path is as follows:
(0,0)->(1,0)->(1,1)->(2,1)->(2,2)->(2,3).
Example 2:

Input:
N=3, M=4
A=[[1,1,1,1],
   [0,0,0,1],
   [0,0,0,1]]
X=0, Y=3
Output:
3
Explanation:
The shortest path is as follows:
(0,0)->(0,1)->(0,2)->(0,3).
"""
#User function Template for python3
from collections import deque
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        def _valid(r, c):
            return r >= 0 and r < N and c >= 0 and c < M
            
        q = deque()
        q.append([0, 0, 0])
        vis = set()
        vis.add((0, 0))
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            r, c, step = q.popleft() 
            if r == X and c == Y:
                return step 
            for i, j in dirs:
                dx = r+i 
                dy = c+j 
                if _valid(dx, dy) and (dx,dy) not in vis and A[dx][dy] == 1:
                    q.append([dx, dy, step+1])
                    vis.add((dx, dy))
        return -1


     