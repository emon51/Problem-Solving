#max sum of non adjacent nums of an array(House robber leetcode)


def f(arr, i=0):
	if i >=len(arr):
		return 0
	#pick
	l = arr[i] + f(arr, i+2)
	#not pick
	r = 0 + f(arr, i+1)
	return max(l, r)
	
if __name__ == "__main__":
	arr = [2, 1, 4, 9]
	print(f(arr))