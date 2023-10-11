class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = float("-inf")
        n = len(seats)
        l = -1
        for r in range(n):
            if seats[r]:
                if l == -1:
                    res = max(res, r)
                else:
                    res = max(res, (r - l) // 2)
                l = r
        if seats[n - 1] == 0:
            res = max(res, r - l)
        return res
