res = []
def f(arr, t, i=0, p=[]):
	global res 
	if i >= len(arr):
		return 
	elif not t:
		res.append(p)
		return 
	elif arr[i] <= t:
		f(arr, t-arr[i], i, p+[arr[i]])
	f(arr, t, i+1, p)
		
if __name__ == "__main__":
	arr = [1, 2, 4, 3, 5]
	t = 6 
	f(arr, t)
	print(res)