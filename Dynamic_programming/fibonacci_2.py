#print nth Fibonacci number

#TC = O(N), SC = O(N) + O(N)
def fibo(n: int, dp={}) ->int:
	if n <= 1:
		return n
	if n in dp:
		return dp[n]
	val = fibo(n-1) + fibo(n-2)
	dp[n] = val 
	return val
	
if __name__ == "__main__":
	n = 50
	print(fibo(n))
	