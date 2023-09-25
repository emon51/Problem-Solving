#print nth Fibonacci number

#TC = O(2^N), SC = O(2^N)
def fibo(n: int) ->int:
	if n <= 1:
		return n
	return fibo(n-1) + fibo(n-2)
	
if __name__ == "__main__":
	n = 5
	print(fibo(n))
	