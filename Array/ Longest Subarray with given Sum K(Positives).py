#codingNinjas: Longest Subarray with given Sum K(Positives)
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    res = 0 
    csm = 0 
    d = {0: -1}
    for i, n in enumerate(a):
        csm += n 
        if csm not in d:
            d[csm] = i 
        if (csm - k) in d:
            res = max(res, i - d[csm-k]) 
    return res

        

