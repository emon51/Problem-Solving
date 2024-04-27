
'''
Problem statement
You are given a two-dimensional array/list of integers consisting of 0s and 1s. In the list, 1 represents land and 0 represents water.

The task is to find the number of DISTINCT islands where a group of connected 1s(horizontally or vertically) forms an island.

Note:
Two islands are considered to be the same if and only if one island is equal to another(not rotated or reflected) i.e if we can translate one island on another without rotating or reflecting then it would be considered as the same islands. 
For example:
1 1 0
0 0 1
0 0 1

In this example, we have two islands and they would be considered as distinct islands as we can not translate them on one another even if they have the same no of 1's.
For example :
1 1 0 0 0 
1 1 0 0 0
0 0 0 1 1
0 0 0 1 1

In this example, we have two islands and they are the same as we can translate one island onto another island, so our answer should be 1.
Detailed explanation ( Input/output format, Notes, Images )
Constraints
 0 <= N <= 1000
 0 <= M <= 1000
 0 <= elements of array <= 1

Time Limit: 1 sec
Sample Input 1:
 4
 5
 1 1 0 1 1
 1 0 0 0 0
 0 0 0 0 1
 1 1 0 1 1
Sample Output 1:
 3
Explanation For Sample Input 1:
Distinct islands in the example above are: 

1st -> at the top left corner; 

2nd -> at the top right corner  

3rd -> at the bottom right corner. 

We ignore the island at the bottom left corner since it is identical to the top right corner.
Sample Input 2:
3
2
1 0
0 1
1 1
Sample Output 2:
2
'''

def distinctIsland(mat,m,n) :

    vis = set()
    dirs = [(1, 0, 'd'), (0, 1, 'r'), (-1, 0, 'u'), (0, -1, 'l')]

    def dfs(r, c, d, p):
        vis.add((r, c))
        p[0] += d
        for i, j, d in dirs:
            dr, dc = r + i, c + j
            if (0 <= dr < m and 0 <= dc < n) and (dr, dc) not in vis and mat[dr][dc] == 1:
                dfs(dr, dc, d, p)
                p[0] += 'b' #backtracking path
    

    res = set()
    for r in range(m):
        for c in range(n):
            if mat[r][c] and (r, c) not in vis:
                cur = ['']
                dfs(r, c, 's', cur)
                res.add(cur[0])
    
    return len(res)
    
