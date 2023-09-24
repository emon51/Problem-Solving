#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		#Bruteforce: sort the array and return arr[n-2], O(nlogn)
		
		#Optimal O(2n)
		first_largest = float("-inf")
		for val in arr:
		    first_largest = max(first_largest, val)
		
		second_largest = float("-inf")
		for val in arr:
		    if val != first_largest:
		        second_largest = max(second_largest, val)
		        
		return second_largest if second_largest != float("-inf") else -1
		
		
		
#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		#O(n)
		a, b = float("-inf"), float("-inf")
		for val in arr:
		    if a <= val:
		        prev_a = a
		        a = val 
		        if prev_a != a:
		            b = prev_a 
		    else:
		        b = max(b, val)
		return b if b != float("-inf") else -1
		
