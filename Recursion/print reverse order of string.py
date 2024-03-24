
def rev(s, i = 0):
    if i == len(s):
        return
    rev(s, i + 1)
    print(s[i], end = '')
    

s = 'google'
rev(s)
