#print nth Fibonacci number

#TC : O(N), SC = O(N)
def fibo(n: int) ->int:
	dp = [-1] * (n+1)
	dp[0] = 0 
	dp[1] = 1 
	for i in range(2, n + 1):
		dp[i] = dp[i-1] + dp[i-2]
	return dp[n]
	
if __name__ == "__main__":
	n = 50
	print(fibo(n))
	