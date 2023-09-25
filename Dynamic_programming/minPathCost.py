#Return min path cost to reach nth stairs
#[1, 2, 3, 4]
#path1 cost : 1+2+3+4 = 10
#path2 cost : 1+3+4 = 8 
#path3 cost : 1+2+4 = 7 
#So min cost = 7
def f(arr: list[int], n: int, cost=0) -> int:
	if n == 0:
		return cost + arr[n]
	if n < 0:
		return float("inf")
	p1=f(arr, n-1, cost+arr[n])
	p2=f(arr, n-2, cost+arr[n])
	return min(p1, p2)
	
if __name__ == "__main__":
	arr = [1, 2, 3, 4]
	print(f(arr, len(arr)-1))
	
	
	
	