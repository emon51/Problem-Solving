
#TLE
def findLCS(m: int, n: int, s1: str, s2: str) -> str:
    
    res = ''
    maxlen = 0

    def fun(i, j, p = ''):
        nonlocal res, maxlen
        if i == m or j == n:
            if maxlen < len(p):
                res = p
                maxlen = len(p)
            return 
        
        if s1[i] == s2[j]:
            fun(i + 1, j + 1, p + s1[i])
        fun(i + 1, j, p)
        fun(i, j + 1, p)

    fun(0, 0)
    return res
        
