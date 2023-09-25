#print 1 to n using recursion 

def f(n):
	if not n:
		return 
	f(n-1)
	print(n)
	
	
if __name__ == "__main__":
	n = 10 
	f(n)