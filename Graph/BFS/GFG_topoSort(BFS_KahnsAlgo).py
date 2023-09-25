from collections import deque 
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        q = deque() 
        indegree = [0] * V
        for node in range(V):
            for ngh in adj[node]:
                indegree[ngh] += 1
        
        res = [] 
        cnt = 0 
        for node in range(V):
            if indegree[node] == 0:
                q.append(node)
        while q:
            node = q.popleft() 
            cnt += 1
            for ngh in adj[node]:
                indegree[ngh] -= 1
                if indegree[ngh] == 0:
                    q.append(ngh)
            res.append(node)
            
        if cnt == V:
            return res 
        #There exist cycle 
        return None