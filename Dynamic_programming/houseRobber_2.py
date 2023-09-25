#max sum of non adjacent nums of an array(House robber leetcode)

#TC = O(N), SC = O(N) + O(N) -> Recursion space O(N), dp space O(N)
def f(arr, i=0, dp={}):
	if i in dp:
		return dp[i]
	if i >=len(arr):
		return 0
	#pick
	l = arr[i] + f(arr, i+2)
	#not pick
	r = 0 + f(arr, i+1)
	val = max(l, r)
	dp[i] = val 
	return val 
	
if __name__ == "__main__":
	arr = [2, 1, 4, 9]
	print(f(arr))