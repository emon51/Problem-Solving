
'''
Problem statement
You are given an array 'ARR' that consists of ‘N’ numbers. Your task is to split the array into 
two non-empty subarrays such that the absolute difference between their sum is minimum. For example,
If the given array is [6,7,1,8,5]. We can split the array into [6,7,1] and [8,5].
Hence the answer will be |14-13| = 1 which is minimum.
'''

def minimumDifference(n, arr):
    
    total = sum(arr)
    res = float('inf')
    csm = 0
    for num in arr:
        csm += num 
        total -= num
        res = min(res, abs(total - csm))
    return res



