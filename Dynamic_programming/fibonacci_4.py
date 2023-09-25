#print nth Fibonacci number

#TC : O(N), SC = O(1)
def fibo(n: int) ->int:
	a = 0 
	b = 1
	for i in range(2, n + 1):
		c = a + b 
		a = b 
		b = c 
	return b
	
if __name__ == "__main__":
	n = 50
	print(fibo(n))
	