
"""
Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 

"""

#without memoization
class Solution:

    def isSubsetSum (self, N, arr, k):

        

        def f(i, k):

            if k == 0:

                return True

            if i == N or k < 0:

                return False

            pick = f(i+1, k - arr[i])
            notPick = f(i+1, k)
            return pick or notPick 

       
        return f(0, k)



#With memoization
class Solution:

    def isSubsetSum (self, N, arr, k):

        

        def f(i, k, dp={}):

            if k == 0:

                return True

            if i == N or k < 0:

                return False

            if (i,k) in dp:

                return dp[(i, k)]

        

            pick = f(i+1, k - arr[i], dp)

            notPick = f(i+1, k, dp)

            val = pick or notPick 

            dp[(i, k)] = val 

            return val 

            

        return f(0, k)

        
"""
Given an array of non-negative integers, and a value sum, count the number of sum equal to given sum. 
"""
class Solution:

    def isSubsetSum (self, N, arr, k):

        

        def f(i, k):

            if k == 0:

                return True

            if i == N or k < 0:

                return False

            pick = f(i+1, k - arr[i])
            notPick = f(i+1, k)
            return pick + notPick 

       
        return f(0, k)



       

        

        





