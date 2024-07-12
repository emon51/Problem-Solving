
'''
Given an array arr of n integers, write a function that returns true if there is a triplet (a, b, c) from the array (where a, b, and c are on different indexes) that satisfies a2 + b2 = c2, otherwise return false.

Example 1:

Input:
N = 5
Arr[] = {3, 2, 4, 6, 5}
Output: Yes
Explanation: a=3, b=4, and c=5 forms a
pythagorean triplet.
Example 2:

Input:
N = 3
Arr[] = {3, 8, 5}
Output: No
Explanation: No such triplet possible.
Your Task:
You don't have to take any input or print any thing. You have to complete the function checkTriplet() which takes an array arr, a single integer n, as input parameters and returns boolean denoting answer to the problem.
Note: The driver will print "Yes" or "No" instead of corresponding to the boolean value returned.

Expected Time Complexity: O(n+max(Arr[i])2)
Expected Auxiliary Space: O(max(Arr[i]))

Constraints:
1 <= n <= 105
'''

#Brute Force. TC: O(N^3)

class Solution:

    def checkTriplet(self,arr, n):
        
        arr.sort(reverse = True )
        for c in range(n):
            for a in range(c + 1, n):
                for b in range(a + 1, n):
                    if arr[c] ** 2 == arr[a] ** 2 + arr[b] ** 2:
                        return True 
        return False


#Brute Force. TC: O(N^2)

class Solution:

    def checkTriplet(self,arr, n):
        
        arr.sort(reverse = True )
        for c in range(n - 2):
            a, b = c + 1, n - 1
            while a < b:
                sq = arr[a] ** 2 + arr[b] ** 2 
                if sq == arr[c] ** 2:
                    return True 
                elif sq < arr[c] ** 2:
                    b -= 1
                else:
                    a += 1
        return False



#Optimal 

class Solution:

	def checkTriplet(self,arr, n):
    	
    	st = set(arr)
    	arr = [num * num for num in st]
    	arr.sort(reverse = True )
    	n = len(arr)
    	
    	for c in range(n - 2):
    	    a, b = c + 1, n - 1
    	    while a < b:
    	        curr = arr[a] + arr[b]
    	        if curr == arr[c]:
    	            return True 
    	        elif curr < arr[c]:
    	            b -= 1
    	        else:
    	            a += 1
    	return False
