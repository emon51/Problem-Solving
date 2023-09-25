#Delete middle of the stack
# [1, 2, 3, 4, 5] --> [1, 2, 4, 5]
"""
arr = [1,2,3,4,5]
mid = len(arr)//2
res = [] 
for i, n in enumerate(arr):
	if i != mid:
		res.append(n)
print(res)
"""
def f(arr: list[int]) -> list[int]:
	n = len(arr) 
	mid = n // 2 - 1
	tmp = [] 
	while mid:
		tmp.append(arr.pop())
		mid -= 1 
	arr.pop() 
	
	while tmp:
		arr.append(tmp.pop())
	
	return arr
	
if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6]
	print(f(arr))