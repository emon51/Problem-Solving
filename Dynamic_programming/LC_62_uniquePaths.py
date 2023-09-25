"""leetcode 62: Unique paths 
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
✓✓✓ Follow up : leetcode: 63
"""
"""
######solution: 01######

def f(i, j, m, n):
	if i == m-1 and j == n-1:
		return 1 
	if i >= m or j >= n:
		return 0 
	down = f(i+1, j, m, n)
	right = f(i, j+1, m, n)
	return down + right
	
if __name__ == "__main__":
	m = 3
	n = 7
	print(f(0, 0, m, n))
"""
"""
#####solution: 02#######

def f(i, j, m, n, dp={}):
	if i == m-1 and j == n-1:
		return 1 
	if i >= m or j >= n:
		return 0 
	if (i, j) in dp:
		return dp[(i, j)]
	down = f(i+1, j, m, n, dp)
	right = f(i, j+1, m, n, dp)
	val = down + right
	dp[(i, j)] = val
	return val 
	
if __name__ == "__main__":
	m = 3
	n = 7
	print(f(0, 0, m, n))
"""
#####solution: 03#######
def solution(m, n):
	dp = [[-1 for _ in range(n)] for _ in range(m)] 
	
	def f(i, j, m, n):
		if i == m-1 and j == n-1:
			return 1 
		if i >= m or j >= n:
			return 0 
		if dp[i][j] != -1:
			return dp[i][j]
		down = f(i+1, j, m, n)
		right = f(i, j+1, m, n)
		val = down + right
		dp[i][j] = val 
		return val
	
	return f(0, 0, m, n)
	
if __name__ == "__main__":
	m = 3
	n = 7
	print(solution(m, n))



















