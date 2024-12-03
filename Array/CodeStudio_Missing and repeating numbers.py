
'''
Problem statement
You are given an array of size ‘N’. The elements of the array are in the range from 1 to ‘N’.

Ideally, the array should contain elements from 1 to ‘N’. But due to some miscalculations, there is a number R in the range [1, N] which appears in the array twice and another number M in the range [1, N] which is missing from the array.

Your task is to find the missing number (M) and the repeating number (R).

For example:
Consider an array of size six. The elements of the array are { 6, 4, 3, 5, 5, 1 }. 
The array should contain elements from one to six. Here, 2 is not present and 5 is occurring twice. Thus, 2 is the missing number (M) and 5 is the repeating number (R). 
Follow Up
Can you do this in linear time and constant additional space? 
'''



def missingAndRepeating(arr, n):
    
    i = 0 
    miss, rep = -1, -1
    while i < n:
        ci = arr[i] - 1
        if arr[i] == i + 1:
            i += 1
        else:
            if arr[i] == arr[ci]:
                rep = arr[i]
                i += 1
            else:
                arr[i], arr[ci] = arr[ci], arr[i]
    for i, num in enumerate(arr):
        if (i + 1) != num:
            miss = (i + 1)
            break 
    return [miss, rep]
