#Generating all subsequences
arr = [1, 2, 3]
def f(i,  p = []):
	print(p)
	for j in range(i, len(arr)):
		f(j + 1, p + [arr[j]])
		
f(0)
