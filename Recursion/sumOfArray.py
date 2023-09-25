def f(arr, n, i=0):
	if i == n:
		return 0 
	return arr[i] + f(arr, n, i+1)
	
if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5]
	print(f(arr, len(arr)))