#sum of 1 to n 

def f(n):
	if not n :
		return 0 
	return n + f(n-1)
	
if __name__ == "__main__":
	n = 3
	print(f(n))
	
def f(n, sm=0):
	if not n:
		return sm 
	return f(n-1, sm+n)
if __name__ == "__main__":
	n = 3
	print(f(n))