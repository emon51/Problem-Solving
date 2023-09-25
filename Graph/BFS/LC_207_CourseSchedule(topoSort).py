#Leetcode: 207_Course Schedule
class Solution:
    def canFinish(self, N: int, prereqs: List[List[int]]) -> bool:
      q = deque() 
      indegree = [0] * N 
      adj_list = { u: [] for u in range(N)}
      
      for u, v in prereqs:
        indegree[u] += 1 
        adj_list[v].append(u)
        
      for course in range(N):
        if indegree[course] == 0:
          q.append(course) 
      
      cnt = 0 
      while q:
        course = q.popleft()
        cnt += 1
        for ngh in adj_list[course]:
          indegree[ngh] -= 1 
          if indegree[ngh] == 0:
            q.append(ngh) 
      
      return cnt == N
        