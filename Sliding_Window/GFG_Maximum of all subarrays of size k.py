#TLE, TC : O(n*k)
class Solution:
    #TLE
    def max_of_subarrays(self,arr,n,k):
        res = []
        for i in range(n-k+1):
            cm = 0
            for j in range(i, k+i):
                cm = max(cm, arr[j])
            res.append(cm)
        return res
                


