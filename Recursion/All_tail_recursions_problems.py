#Find average of the array using tail_recursion
def find_average(arr, index, sum):
  if index == len(arr):
    return sum / len(arr)
  else:
    return find_average(arr, index + 1, sum + arr[index])

# Example usage
my_arr = [1, 2, 3, 4, 5]
average = find_average(my_arr, 0, 0)
print(average)


#Using tail_recursion find the array sum

def fun(arr, sm = 0, i = 0):
    if i == len(arr):
        return sm
    return fun(arr, sm + arr[i], i + 1)
    

arr = [1, 2, 3]
res = fun(arr)
print(res)

#Using tail_recursion_finding_minimum of the array


def find_min(arr, i = 0, minn = float('inf')):
    if i == len(arr):
        return minn
    minn = min(minn, arr[i])
    return find_min(arr, i + 1, minn)
    

arr = [3, 1, 2, 4, 5, 7, 6]
res = find_min(arr)
print(res)

#Using tail_recursion_finding_minimum and maximum together from the array


def find_min(arr, i = 0, minn = float('inf'), maxx = float('-inf')):
    if i == len(arr):
        return (minn, maxx)
    minn = min(minn, arr[i])
    maxx = max(maxx, arr[i])
    return find_min(arr, i + 1, minn, maxx)
    

arr = [3, 1, 2, 4, 5, 7, 6]
res = find_min(arr)
print(res)
















