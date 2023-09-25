"""
Leetcode: 
70. Climbing Stairs(Easy)
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
#Brute Force, TC : O(2^N), SC : O(2^N)
def fun1(n: int) -> int:
	if n == 0:
		return 1 
	if n < 0:
		return 0 
	return fun1(n-1) + fun1(n-2)
	
#Optimal solution using memo
def fun2(n: int, dp={}) -> int:
	if n == 0:
		return 1 
	if n < 0:
		return 0 
	if n in dp:
		return dp[n]
	val = fun2(n-1) + fun2(n-2)
	dp[n] = val 
	return val

if __name__ == "__main__":
	n = 50
	#print(fun1(n))
	print(fun2(n))