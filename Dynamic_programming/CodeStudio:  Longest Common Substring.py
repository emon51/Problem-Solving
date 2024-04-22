
#Brute Force
"""
    Time complexity: O((N * M * min(N, M))
    Space complexity: O(1)
    
    Where 'N' and 'M' are the lengths of the two strings.
"""
#Longest common Substring
def lcs(s1: str, s2: str) -> int:
    ans = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            k = 0
            while ((i + k) < len(s1) and (j + k) < len(s2) and s1[i + k] == s2[j + k]):
                k = k + 1
            ans = max(ans, k)
    return ans


