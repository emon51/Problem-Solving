#Generating all subsequences

#Code1
arr = [1, 2, 3]
def fun(i, p = []):
	if i >= len(arr):
	     print(p)
	     return
	#pick	
	fun(i+1, p + [arr[i]])
	#not_pick
	fun(i+1, p)
	
fun(0)

#COde2
arr = [1, 2, 3]
def fun(i,  p = []):
	print(p)
	for j in range(i, len(arr)):
		fun(j + 1, p + [arr[j]])
		
fun(0)
