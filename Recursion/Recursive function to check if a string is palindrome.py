

flag = True 
def fun(s, n, i = 0):
    global flag
    if i == n:
        return 
    fun(s, n, i + 1)
    flag = flag and s[n - i - 1] == s[i]
    
s = 'aba'
res = fun(s, len(s))
print(flag)
    

    
