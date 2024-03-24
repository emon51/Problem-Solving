
def fun(n):
    if n == 0:
        return 0
    
    return (1 & n) + fun(n >> 1)
    

n = 2147483645
res = fun(n)
print(res)
