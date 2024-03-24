
def find_average(arr, index, sum):
  if index == len(arr):
    return sum / len(arr)
  else:
    return find_average(arr, index + 1, sum + arr[index])

# Example usage
my_arr = [1, 2, 3, 4, 5]
average = find_average(my_arr, 0, 0)
print(average)
