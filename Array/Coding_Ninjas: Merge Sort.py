'''
Problem statement
You are given the starting 'l' and the ending 'r' positions of the array 'ARR'.

You must sort the elements between 'l' and 'r'.
'''
#1
def mergeSort(arr: [int], l: int, r: int):
    
    def buble_sort(arr, l, r):
        for i in range(l, r):
            for j in range(l, r - l - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    buble_sort(arr, l, r)


#2
def mergeSort(arr: [int], l: int, r: int):
    
    def merge(arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        res = []
        i, j = 0, 0 
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        if i < n1:
            res.extend(arr1[i: ])
        elif j < n2:
            res.extend(arr2[j: ])
        return res

    def merge_sort(arr):
        if not arr or len(arr) == 1:
            return arr
        mid = (len(arr)) // 2
        left = merge_sort(arr[: mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)


    a = arr[l: r + 1]
    sorted_a = merge_sort(a)
    arr[l: r + 1] = sorted_a
    
