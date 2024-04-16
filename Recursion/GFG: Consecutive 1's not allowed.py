
'''
Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s. Output your answer modulo 109 + 7.

Example 1:

Input:
N = 3
Output: 5
Explanation:
5 strings are (000,
001, 010, 100, 101).
Example 2:

Input:
N = 2
Output: 3
Explanation: 
3 strings are (00,01,10).
Your Task:
You don't have to print answer or take inputs. Complete the function countStrings() which takes single integer n, as input parameters and returns an integer denoting the answer. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 105
'''

#Brute Force
class Solution:

  def countStrings(self, n):

    def fun(s, n):
      if len(s) == n:
        return 1
      l, r = 0, 0
      if not s:
        l = fun(s + '0', n)
        r = fun(s + '1', n)
      else:
        if s[-1] != '1':
          l = fun(s + '1', n)
        r = fun(s + '0', n)
      return (l + r)

    return fun('', n)

#Optized --> It's a observational problem, n = 0 -->  0, n = 1 --> 2, n = 2 --> 3, n == 3 --> 5 it follws fibonacci pattern

class Solution:

	def countStrings(self,n):
    	
    	if n == 1:
    	    return 2 #0, 1
    	if n == 2:
    	    return 3
    	a, b = 2, 3
    	for _ in range(2, n):
    	    c = a + b
    	    a = b
    	    b = c
    	return b % (10 ** 9 + 7)

#Accepted
#User function Template for python3
class Solution:

	def countStrings(self,n):
    	mod = (10 ** 9 + 7)
    	if n == 1:
    	    return 2 #0, 1
    	if n == 2:
    	    return 3
    	a, b = 2, 3
    	for _ in range(2, n):
    	    c = a + b
    	    a = b % mod
    	    b = c % mod
    	return b % mod
