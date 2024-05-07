
'''
Given a value V and array coins[] of size M, the task is to make the change for V cents, given that you have an infinite supply of each of coins{coins1, coins2, ..., coinsm} valued coins. Find the minimum number of coins to make the change. If not possible to make change then return -1.


Example 1:

Input: V = 30, M = 3, coins[] = {25, 10, 5}
Output: 2
Explanation: Use one 25 cent coin
and one 5 cent coin
Example 2:
Input: V = 11, M = 4,coins[] = {9, 6, 5, 1} 
Output: 2 
Explanation: Use one 6 cent coin
and one 5 cent coin

Your Task:  
You don't need to read input or print anything. Complete the function minCoins() which takes V, M and array coins as input parameters and returns the answer.

Expected Time Complexity: O(V*M)
Expected Auxiliary Space: O(V)

Constraints:
1 ≤ V*M ≤ 106
All array elements are distinct
'''
#DP --> TLE
class Solution:
	def minCoins(self, coins, M, V):
		
		def fun(i, p, dp = {}):
		    if (i, p) in dp:
		        return dp[(i, p)]
		    if p == 0:
		        return 0
		    if i == M or p < 0:
		        return float('inf')
		    pick = float('inf')
		    if coins[i] <= p:
		        pick =  1 + fun(i, p - coins[i], dp)
		    notpick = fun(i + 1, p, dp)
		    val = min(pick, notpick)
		    dp[(i, p)] = val 
		    return val
	    res = fun(0, V)
	    return res if res != float('inf') else -1

#Greedy --> Accepted



