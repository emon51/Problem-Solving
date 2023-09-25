"""
[1, 2, 2]
[[1, 2, 2], [1, 2], [1, 2], [1], [2, 2], [2], [2], []]
                ____   ____
"""
res = []
def f(arr, i=0, p=[]):
	global res 
	if i >= len(arr):
		res.append(p)
		return 
	#pick current number 
	f(arr, i+1, p+[arr[i]])
	#skip current number 
	f(arr, i+1, p)
	
if __name__ == "__main__":
	arr = [1, 2, 2]
	f(arr)
	print(res)
	