

#Brute Force
def longestPalindromeSubsequence(s):
    
    n = len(s)
    res = 0
    for i in range(n):

        l, r = i, i
        curr_len = 0
        while l >= 0 and r < n and s[l] == s[r]:
            curr_len += 1
            l -= 1
            r += 1
        res = max(res, curr_len)

        l, r = i, i + 1
        curr_len = 0
        while l >= 0 and r < n and s[l] == s[r]:
            curr_len += 1
            l -= 1
            r += 1
        res = max(res, curr_len)
    
    return res
        

