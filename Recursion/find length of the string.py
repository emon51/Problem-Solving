def length(s, i = 0):
    if i == len(s):
        return 0
    
    return 1 + length(s, i + 1)
    

s = 'google'
res = length(s)
print(res)
