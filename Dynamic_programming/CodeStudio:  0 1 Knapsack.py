
'''
Problem statement
A thief is robbing a store and can carry a maximal weight of W into his knapsack. There are N items and the ith item weighs wi and is of value vi. 
Considering the constraints of the maximum weight that a knapsack can carry, you have to find and return the maximum value that a thief can generate by stealing items.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= N <= 10^2
1<= wi <= 50
1 <= vi <= 10^2
1 <= W <= 10^3

Time Limit: 1 second
Sample Input:
1 
4
1 2 4 5
5 4 8 6
5
Sample Output:
13
'''
#TLE
def solution(n, wts, vals, cap):

    def fun(i, cap):
        if i == n or cap <= 0:
            return 0
        f1, f2 = 0, 0
        if wts[i] <= cap:
            f1 = vals[i] + fun(i + 1, cap - wts[i])
        f2 = 0 + fun(i + 1, cap)
        return max(f1, f2)
    
    return fun(0, cap)
      

t = int(input())
for _ in range(t):
    n = int(input())
    wts = list(map(int, input().split()))
    vals = list(map(int, input().split()))
    cap = int(input())
    res = solution(n, wts, vals, cap)
    print(res)
  
#=======================================================#

#Accepted
def solution(n, wts, vals, cap):

    def fun(i, cap, dp = {}):
        if (i, cap) in dp:
            return dp[(i, cap)]
        if i == n or cap <= 0:
            return 0
        f1, f2 = 0, 0
        if wts[i] <= cap:
            f1 = vals[i] + fun(i + 1, cap - wts[i])
        f2 = 0 + fun(i + 1, cap)
        val = max(f1, f2)
        dp[(i, cap)] = val
        return val
    
    return fun(0, cap)


t = int(input())
for _ in range(t):
    n = int(input())
    wts = list(map(int, input().split()))
    vals = list(map(int, input().split()))
    cap = int(input())
    res = solution(n, wts, vals, cap)
    print(res)
