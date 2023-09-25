#print subsequence whose sum  is k 

def f(arr: list[int], k: int, p=[],sm=0) -> None:
	if not arr and sm == k:
		print(p)
		return 
	if not arr:
		return 
	#taking current number
	f(arr[1:], k, p+[arr[0]], sm+arr[0]) 
	#skipping current number
	f(arr[1:], k, p, sm)
	
if __name__ == "__main__":
	arr = [1, 2, 3]
	k = 3
	f(arr, k)