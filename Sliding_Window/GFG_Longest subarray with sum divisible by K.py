"""
Given an array arr containing N integers and a positive integer K, find the length of the longest sub array with sum of the elements divisible by the given value K.

Example 1:

Input:
N = 6, K = 3
arr[] = {2, 7, 6, 1, 4, 5}
Output: 
4
Explanation:
The subarray is {7, 6, 1, 4} with sum 18, which is divisible by 3.
Example 2:

Input:
N = 7, K = 3
arr[] = {-2, 2, -5, 12, -11, -1, 7}
Output: 
5
Explanation:
The subarray is {2,-5,12,-11,-1} with sum -3, which is divisible by 3.
"""

#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, k) : 
	    
	    csm = 0
	    d = {0: -1}
	    res = 0 
	    for i, num in enumerate(arr):
	        csm += num
	        rem = csm % k
	        if rem in d:
	            res = max(res, i - d[rem])
	        else:
	            d[rem] = i 
	    return res
