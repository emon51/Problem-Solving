"""
Given an undirected graph with V vertices. We say two vertices u and v belong to a single province if there is a path from u to v or v to u. Your task is to find the number of provinces.

Note: A province is a group of directly or indirectly connected cities and no other cities outside of the group.

Example 1:

Input:
[
 [1, 0, 1],
 [0, 1, 0],
 [1, 0, 1]
]

Output:
2
Explanation:
The graph clearly has 2 Provinces [1,3] and [2]. As city 1 and city 3 has a path between them they belong to a single province. City 2 has no path to city 1 or city 3 hence it belongs to another province.
Example 2:
Input:
[
 [1, 1],
 [1, 1]
]

Output :
1

Your Task:  
You don't need to read input or print anything. Your task is to complete the function numProvinces() which takes an integer V and an adjacency matrix adj as input and returns the number of provinces. adj[i][j] = 1, if nodes i and j are connected and adj[i][j] = 0, if not connected.


Expected Time Complexity: O(V2)
Expected Auxiliary Space: O(V)
"""
#BFS
#User function Template for python3
from collections import deque
class Solution:
    def numProvinces(self, adj, V):
        
        vis = [0] * V
        def bfs(adj, src):
            q = deque()
            q.append(src)
            vis[src] = 1
            while q:
                p = q.popleft()
                for v in adj[p]:
                    if not vis[v]:
                        q.append(v)
                        vis[v] = 1
            return 1
            
        #create adj_list from given adj_matrix 
        adj_list = { v: [] for v in range(V)}
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1:
                   adj_list[i].append(j)
                   adj_list[j].append(i)
        
        res = 0
        for v in range(V):
            if not vis[v]:
                res += bfs(adj_list, v)
        return res