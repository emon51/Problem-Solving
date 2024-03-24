

def digitSum(n):
    if n == 0:
        return 0
    return (n % 10) + digitSum(n // 10)
    
n = 1234
print(digitSum(n))
