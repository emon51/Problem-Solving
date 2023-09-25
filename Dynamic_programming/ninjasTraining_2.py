#problem : Ninjas training (coding ninjas)

def f(arr: list[list[int]], day=0, last=-1,dp={}):
	if (day, last) in dp:
		return dp[(day, last)]
	if day >= len(arr):
		return 0
	res = 0
	for i in range(3):
		if i == last:
			continue
		curr = arr[day][i] + f(arr, day+1, i)
		res = max(res, curr)
	dp[(day, last)] = res
	return res
		
if __name__ == "__main__":
	arr = [[2, 1, 3], [5, 4, 7], [1, 6, 2]]
	print(f(arr))
		