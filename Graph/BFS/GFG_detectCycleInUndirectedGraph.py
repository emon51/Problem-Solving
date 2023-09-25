"""
Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. Graph is in the form of adjacency list where adj[i] contains all the nodes ith node is having edge with.

Example 1:

Input:  
V = 5, E = 5
adj = {{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}} 
Output: 1
Explanation: 

1->2->3->4->1 is a cycle.
Example 2:

Input: 
V = 4, E = 2
adj = {{}, {2}, {1, 3}, {2}}
Output: 0
Explanation: 

No cycle in the graph.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function isCycle() which takes V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the undirected graph contains any cycle or not, return 1 if a cycle is present else return 0.

NOTE: The adjacency list denotes the edges of the graph where edges[i] stores all other vertices to which ith vertex is connected.
"""

from typing import List

from collections import deque



class Solution:

    #Function to detect cycle in an undirected graph.

	def isCycle(self, V: int, adj: List[List[int]]) -> bool:

	    vis = set()

	    def bfs(src):

	       q = deque() 

	       q.append((src, -1)) # vertex, parent

	       vis.add(src)

	       while q:

	           v, par = q.popleft()

	           for vertex in adj[v]:

	              if vertex not in vis:

	                 q.append((vertex, v))

	                 vis.add(vertex)

	              else:

	                  if vertex != par:

	                      return True 

	       return False 

	       

	    for v in range(V):

	        if v not in vis:

	            if bfs(v) == True:

	                return True

	    return False 
