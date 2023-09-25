#Leetcode: 802_Find Eventual Safe States
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
      
      vis, path_vis = set(), set();
      safe_nodes = []
      
      def dfs(node):
        vis.add(node) 
        path_vis.add(node) 
        for v in graph[node]:
          if v not in vis:
            if dfs(v) == True:
              return True  
          else:
            if v in path_vis: #cycle exits
              return True
        
        path_vis.remove(node) 
        safe_nodes.append(node) 
        return False
      
      for node in range(len(graph)):
        if node not in vis:
          dfs(node) 
      
      return sorted(safe_nodes)
        
        
        
        