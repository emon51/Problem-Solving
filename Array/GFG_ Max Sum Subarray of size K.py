#Max Sum Subarray of size K(positives)

#TLE, TC: O(n*k)
class Solution:
    def maximumSumSubarray (self,k,arr,n):
        res = 0
        for i in range(n-k+1):

            csm = 0
            for j in range(i, k+i):
                csm += arr[j]
            res = max(res, csm)
        return res
        
#Accepted, TC: O(n)
class Solution:
    def maximumSumSubarray (self,k,arr,n):
        res = 0; l = 0; csm = 0;
        for r in range(n):
            csm += arr[r]
            if (r - l + 1) == k:
                res = max(res, csm)
                csm -= arr[l]
                l += 1
            
        return res
        
        
