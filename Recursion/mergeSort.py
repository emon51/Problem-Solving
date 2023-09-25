def merge(L: list[int], R: list[int]) -> list[int]:
	res = [] 
	i, j = 0, 0 
	while i<len(L) and j<len(R):
		if L[i] <= R[j]:
			res.append(L[i])
			i += 1 
		else:
			res.append(R[j])
			j += 1 
	
	while i<len(L):
		res.append(L[i])
		i += 1 
	while j<len(R):
		res.append(R[j])
		j += 1 
		
	return res
	
def merge_sort(arr: list[int]) -> list[int]:
	if len(arr) <= 1:
		return arr
	mid = len(arr) // 2
	L = merge_sort(arr[:mid])
	R = merge_sort(arr[mid:])
	return merge(L, R)
	
if __name__ == "__main__":
	arr = [4, 1, 3, 2, 7, 6, 5]
	print(merge_sort(arr))