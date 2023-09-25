"""
[1, 2, 2]
[[1, 2, 2], [1, 2], [1, 2], [1], [2, 2], [2], [2], []]
                ____   ____
output must not contains duplicate subset 
"""


res = set()
def f(arr, i=0, p=()):
	global res 
	if i >= len(arr):
		res.add(p)
		return 
	#pick current number 
	f(arr, i+1, p+(arr[i], ))
	#skip current number 
	f(arr, i+1, p)
	
if __name__ == "__main__":
	arr = [1, 2, 2]
	f(arr)
	res =[list(a) for a in res]
	print(res)
	