#subset sum 
#[1, 3, 2] --> [0, 1, 3, 2, 4, 3, 5, 6]

res = []
def f(arr, i=0, sm=0):
	global res 
	if i >= len(arr):
		res.append(sm)
		return 
	#pick current number 
	f(arr, i+1, sm+arr[i])
	#skip current number 
	f(arr, i+1, sm)
	
if __name__ == "__main__":
	arr = [1, 3, 2]
	f(arr)
	print(res)
	
