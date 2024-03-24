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


#Print Fibonacci Series In Reverse Order Using Tecursion
