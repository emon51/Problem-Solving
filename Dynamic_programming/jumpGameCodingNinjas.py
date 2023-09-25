#Jump game from coding Ninjas 
def f(arr: list[int], n: int, cost=0, dp={}) ->int:
	if n in dp:
		return dp[n]
	if n == 0:
		return cost 
	if n < 0:
		return float("inf")
	l=f(arr, n-1, cost+abs(arr[n]-arr[n-1]),dp)
	r=f(arr, n-2, cost+abs(arr[n]-arr[n-2]),dp)
	val = min(l, r)
	dp[n] = val
	return val 
	
if __name__ == "__main__":
	size = 500
	arr = [n for n in range(size)]
	print(f(arr, len(arr)-1))
	
	
	
	