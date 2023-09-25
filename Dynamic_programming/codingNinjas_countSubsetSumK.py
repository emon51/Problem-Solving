
def findWays(arr: List[int], k: int) -> int:

    def fun(i, k, dp = {}):
        if k == 0:
            return 1 
        if i == len(arr) or k < 0:
            return 0
        if (i, k) in dp:
            return dp[(i, k)]
        pick = fun(i + 1, k - arr[i])
        notPick = fun(i + 1, k)
        val = pick + notPick
        dp[(i, k)] = val
        return val
    return fun(0, k) % (10**9 + 7)
    