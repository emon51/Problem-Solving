#print all subsequence 

def f(arr : list[int], p=[]) -> None:
	if not arr:
		print(p)
		return
	#taking the current number
	f(arr[1:], p+[arr[0]]) 
	#skipping the current number
	f(arr[1:], p)
	
if __name__ == "__main__":
	arr = [1, 2, 3]
	f(arr)