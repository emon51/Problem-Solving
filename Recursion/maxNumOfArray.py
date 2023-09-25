#find largest num using recursion from an array
"""
res = float("-inf")

def f(arr, N, i = 0):
	global res
	if i >= N:
		return
	res = max(res, arr[i])
	f(arr, n, i + 1)
"""
def ff(arr, N, i=0):
	if i >= N:
		return float('-inf')
	return max(arr[i], ff(arr, N, i+1))
if __name__ == "__main__":
	arr = [1,3,6,18,0,5]
	#f(arr, len(arr))
	#print(res)
	print(ff(arr, len(arr)))