

def quick_sort(arr):
    if len(arr) in (0, 1):
        return arr 
    pivot = arr[0]
    left = [num for num in arr if num < pivot]
    right = [num for num in arr if num > pivot]
    mid = [num for num in arr if num == pivot]
    return quick_sort(left) + mid + quick_sort(right)


if __name__ == '__main__':
    nums = [3, 1, 4, 6, 5, 2]
    res = quick_sort(nums)
    print(res)
