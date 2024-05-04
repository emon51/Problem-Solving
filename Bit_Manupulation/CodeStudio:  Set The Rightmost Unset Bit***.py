
'''
Problem statement
The problem is to find the rightmost bit of a non-negative number 'N' that is currently unset (i.e., has a value of 0) in its binary representation and set it to 1.



Return the number after setting the rightmost unset bit of 'N'. If there are no unset bits in N's binary representation, then the number should remain unchanged.



Example:
N = 5
Output: 7
Explanation: The binary representation of 5 is 101. After setting the rightmost unset bit it becomes 111 which is 7.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
10
Sample Output 1:
11
Explanation Of Sample Input 1:
N=10
The binary representation of 10 is 1010. After setting the rightmost unset bit it becomes 1011 which is 11.
Sample Input 2:
7
Sample Output 2:
7
Explanation Of Sample Input 2:
N=7
The binary representation of 7 is 111. As there is no unset bit it remains the same.
Constraints:
1 <= N <= 10^9
Time Limit: 1 sec

'''


def setBits(n : int) -> int:

    m = n 
    unset = 0
    while m:
        unset += 1 if m & 1 == 0 else 0
        m >>= 1
    if unset == 0:
        return n
    return n | (n + 1)



#Note: Clear/unset right most setbit --> n & (n - 1) ***


