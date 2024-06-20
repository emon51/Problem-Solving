
#Brute Force 
class Solution:
    def minDays(self, arr: List[int], M: int, K: int) -> int:

        for d in range(min(arr), max(arr) + 1):
            count = 0 
            m = M
            k = K
            for bd in arr:
                if bd <= d:
                    count += 1
                else:
                    count = 0
                if count == k:
                    m -= 1
                    count = 0
            if m <= 0:
                return d 
        return -1


#OPtimal
class Solution:
    def minDays(self, arr: List[int], M: int, K: int) -> int:

        l, r = min(arr), max(arr)
        res = -1
        while l <= r:
            mid = (l + r) // 2             
            count = 0 
            m = M
            k = K
            for bd in arr:
                if bd <= mid:
                    count += 1
                else:
                    count = 0
                if count == k:
                    m -= 1
                    count = 0
            if m <= 0:
                res = mid 
                r = mid - 1
            else:
                l = mid + 1
        return res
        
