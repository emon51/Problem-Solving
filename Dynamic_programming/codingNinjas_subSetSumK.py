#constraints : 0 <= arr[i] 

def f(arr, i, k):
	if i == 0:
		return arr[0] == k
	if k < 0:
		return False 
		
	pick = f(arr, i-1, k-arr[i])
	notPick = f(arr, i-1, k)
	
	return pick or notPick
	
if __name__ == "__main__":
	arr = [1, 2, 3, 4]
	k = 
	print(f(arr, len(arr)-1, k))
	