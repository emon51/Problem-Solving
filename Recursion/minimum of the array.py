
#Using tail recursion, TC: O(N)
def fun(arr, i, minn = float('inf')):
    if i == len(arr):
        return minn
    return fun(arr, i + 1, min(minn, arr[i]))


arr = [4, -3, 2, 0, 7, 9]
print(fun(arr, 0))

#TC: logN
def fun(arr):
    if not arr:
        return float('inf')
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    left = fun(arr[: mid])
    right = fun(arr[mid:])
    return min(left, right)


arr = [4, -3, 2, 0, 7, 9]
print(fun(arr))
