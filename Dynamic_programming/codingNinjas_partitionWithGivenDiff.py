#Gives wrong answer 
def countPartitions(n: int, d: int, arr: List[int]) -> int:
    
    target = (sum(arr) - d) / 2

    def fun(i, k):
        if k == 0:
            return 1
        if i == len(arr) or k < 0:
            return 0
        pick = fun(i + 1, k - arr[i])
        notPick = fun(i + 1, k)
        return pick + notPick
    return fun(0, target)
    