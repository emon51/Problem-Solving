#TC = O(N), SC = O(1)
def f(arr):
	n = len(arr)
	if n == 1:
		return arr[0]
	a = arr[0]
	b = max(arr[0], arr[1])
	for i in range(2, n):
		c = max(arr[i]+a, b) 
		a = b 
		b = c
	return b
	
if __name__ == "__main__":
	arr = [2, 1, 4, 9]
	print(f(arr))
	