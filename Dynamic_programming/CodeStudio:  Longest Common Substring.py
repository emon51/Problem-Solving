
#TLE
def lcs(s1: str, s2: str) -> int:
    
    m, n = len(s1), len(s2)
    def fun(i, j, count):
        if i == m or j == n:
            return count

        if s1[i] == s2[j]:
            count = fun(i + 1, j + 1, count + 1)
    
        f1 = fun(i + 1, j, 0)
        f2 = fun(i, j + 1, 0)

        return max(f1, f2, count)

    return fun(0, 0, 0)
