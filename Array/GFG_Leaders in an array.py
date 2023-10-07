class Solution:
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        
        res = []
        prev_most = float("-inf")
        for i in range(N-1, -1, -1):
            if A[i] >= prev_most:
                res.append(A[i])
                prev_most = A[i]
        return res[::-1]
