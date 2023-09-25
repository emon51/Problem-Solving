#print name n times using recursion 

def f(name, n):
	if not n:
		return 
	print(name)
	f(name, n-1)
	
if __name__ == "__main__":
	name = "Emon"
	n = 10
	f(name, n)