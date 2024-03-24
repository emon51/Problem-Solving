#Tail_recursion
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
