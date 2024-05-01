#Leetcode: 1319_Number of Operations to Make Network Connected
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
      
      #Not enough edges to connect all vertices
      if len(connections) < n-1:
        return -1
        
      adj = {u: [] for u in range(n)} 
      
      for u, v in connections:
        adj[u].append(v) 
        adj[v].append(u) 
        
      vis = set()
        
      def bfs(src):
        q = deque() 
        q.append(src) 
        vis.add(src) 
        
        while q: 
          p = q.popleft() 
          for v in adj[p]:
            if v not in vis:
              q.append(v) 
              vis.add(v) 
      
      cnt = 0 
      for u in range(n):
        if u not in vis:
          bfs(u) 
          cnt += 1
      
      return cnt - 1

#DFS
def makeGraphConnected(n, edges, m):

    if m < (n - 1):
        return -1
    
    adj = {u: [] for u in range(1, n + 1)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    vis = set()

    def dfs(u):
        vis.add(u)
        for v in adj[u]:
            if v not in vis:
                dfs(v)
    
    components = 0
    for u in range(1, n + 1):
        if u not in vis:
            dfs(u)
            components += 1
    return components - 1
    


        
        
