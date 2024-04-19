
'''
Problem Statement:

Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the frog can climb either one or two steps. 
A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), 
where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.

Examples
Sample Input 1:
2
4
10 20 30 10
3
10 50 10
Sample Output 1:
20
0
Explanation of sample input 1:
For the first test case,
The frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost).
Then a jump from the 2nd stair to the last stair (|10-20| = 10 energy lost).
So, the total energy lost is 20 which is the minimum. 
Hence, the answer is 20.

For the second test case:
The frog can jump from 1st stair to 3rd stair (|10-10| = 0 energy lost).
So, the total energy lost is 0 which is the minimum. 
Hence, the answer is 0.
Sample Input 2:
2
8
7 4 4 2 6 6 3 4 
6
4 8 3 10 4 4 
Sample Output 2:
7
2
'''


def frogJump(n: int, arr: List[int]) -> int:

    def dfs(n, dp = {}):
        if n in dp:
            return dp[n]
        if n == 0:
            return 0
        
        f1 = abs(arr[n] - arr[n - 1]) + dfs(n - 1, dp)
        f2 = float('inf')
        if n > 1:
            f2 = abs(arr[n] - arr[n - 2]) + dfs(n - 2, dp)
        val = min(f1, f2)
        dp[n] = val 
        return val
    
    return dfs(n-1)

#Bottom-Up
def frogJump(n: int, arr: List[int]) -> int:

    dp = [-1] * n 
    dp[0] = 0
    for i in range(1, n):
        f1 = dp[i - 1] + abs(arr[i] - arr[i - 1])
        f2 = float('inf')
        if i > 1:
            f2 = dp[i - 2] + abs(arr[i] - arr[i - 2])
        dp[i] = min(f1, f2)
    
    return dp[n -1]
