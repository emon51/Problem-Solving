
Problem link: https://www.geeksforgeeks.org/problems/travelling-salesman-problem2732/1

#Brute Force (TLE)

class Solution:
    def tsp(self, cost):
        
        n = len(cost)
        all_visited = (1 << n) - 1

        def dfs(pos, mask):
            if mask == all_visited:
                return cost[pos][0]
            res = float('inf')
            for city in range(n):
                if (mask & (1 << city)) == 0:
                    res = min(res, cost[pos][city] + dfs(city, mask | (1 << city)))
            return res 
                    
         

        return dfs(0, 1)

#DP (TLE)

class Solution:
    def tsp(self, cost):
        
        n =len(cost)
        all_visited = (1 << n) - 1

        def dfs(pos, mask, dp):
            if (pos, mask) in dp:
                return dp[(pos, mask)]
            if mask == all_visited:
                return cost[pos][0]
            res = float('inf')
            for city in range(n):
                if (mask & (1 << city)) == 0:
                    res = min(res, cost[pos][city] + dfs(city, mask | (1 << city), dp))
            dp[(pos, mask)] = res
            return res 
                    
         

        return dfs(0, 1, {})
