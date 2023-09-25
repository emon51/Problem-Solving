#Return all path to reach nth stairs
#[1, 2, 3, 4]

def f(arr, n, p=[]):
	if n == 0:
		p += [arr[n]]
		print(p)
		return 
	if n < 0:
		return 
	f(arr, n-1, p+[arr[n]])
	f(arr, n-2, p+[arr[n]])
	
if __name__ == "__main__":
	arr = [1, 2, 3, 4]
	f(arr, len(arr)-1)
	
	
	
	
	