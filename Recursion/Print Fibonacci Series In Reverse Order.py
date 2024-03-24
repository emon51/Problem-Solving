#Print Fibonacci Series In Normal Order.
def fun(n):
    a, b = 1, 1
    while n:
        print(a, end = ' ')
        a, b = b, a + b
        n -= 1
n = 10
fun(n)

#Print Fibonacci Series In Normal Order Using Recursion
def fun(n, a = 1, b = 1):
    if n == 0:
        return 
    print(a, end = ' ')
    fun(n - 1, b, a + b)
n = 10
fun(n)

#Print Fibonacci Series In Reverse Order Using Tecursion

def fun(n, a = 1, b = 1):
    if n == 0:
        return 
    fun(n - 1, b, a + b)
    print(a, end = ' ')
n = 10
fun(n)
