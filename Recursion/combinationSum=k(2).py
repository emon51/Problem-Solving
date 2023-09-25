res = []
def f(arr, t, i=0, p=[]):
	global res 
	if i >= len(arr):
		return 
	elif not t:
		res.append(p)
		return 
	elif arr[i] <= t:
		f(arr, t-arr[i],1+ i, p+[arr[i]])
	f(arr, t, i+1, p)
		
if __name__ == "__main__":
	arr = [10, 1, 2, 7, 6, 1, 5]
	t = 8
	f(arr, t)
	print(res)