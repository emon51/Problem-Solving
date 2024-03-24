
#iteratively(logn)

def decimalToBinary(n):
  stack = []
  while n:
    remainder = n % 2
    stack.append(remainder)
    n //= 2

  res = 0
  while stack:
    res = res * 10 + stack.pop()

  return res

############################################################################################

#recursively_1(logn)

res = 0
def decimalToBinary(n):
    global res
    if n == 0:
        return 0
    decimalToBinary(n // 2)
    res = res * 10 + n % 2
    

n = 10
decimalToBinary(n)
print(res)
#===================================================================================================

#recursively_2(logn)


def decimalToBinary(n):
    if n == 0:
        return 0
    return (n % 2) + 10 * decimalToBinary(n // 2)
    

n = 19
res = decimalToBinary(n)
print(res)





















