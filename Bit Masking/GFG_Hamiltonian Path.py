
Problem link:  https://www.geeksforgeeks.org/problems/hamiltonian-path2522/1

#Brute Force

from collections import deque, defaultdict
class Solution:
    def check(self, n, m, edges): 
        
        adj = defaultdict(lambda : [])
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque()
        for node in range(1, n + 1):
            q.append([node, 1, set([node])])
        
        while q:
            node, count, vis = q.popleft()
            if count == n:
                return 1
            for ngh in adj[node]:
                if ngh not in vis:
                    new_vis = vis.copy()
                    new_vis.add(ngh)
                    q.append([ngh, count + 1, new_vis])
                    
        return 0

#Optimal (Using Bit Masking) 

from collections import deque, defaultdict
class Solution:
    def check(self, n, m, edges): 
        
        adj = defaultdict(lambda : []) #or defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque() #[node, mask]
        target_mask = (1 << n) - 1
        for node in range(1, n + 1):
            q.append([node, 1 << (node - 1)]) #Since virtices started from 1  
        
        while q:
            node, mask = q.popleft()
            if mask == target_mask:
                return 1
            for ngh in adj[node]:
                if mask & (1 << (ngh - 1)) == 0:
                    q.append([ngh, mask | (1 << (ngh - 1))])
        return 0
