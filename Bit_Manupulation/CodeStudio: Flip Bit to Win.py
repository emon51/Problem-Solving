'''
Problem statement
Ninjas are often known for their stealth execution and accuracy to get the job done right. While honing their art of moving through dense forests stealthily, they need the maximum number of continuous trees one after the other for practicing.

Trees are represented by 1s and empty places by 0s (basically a binary representation of a given integer). You are also given an extra tree which you can plant at any empty place (i.e. you can flip one of the zeroes in the binary representation to 1). The tree should be planted such that the maximum number of consecutive trees is maximized.

Your task is to report the maximum number of consecutive trees after plantation.

Note:

You may also choose not to plant that extra tree at all.
For Example:
Input: 54
Output: 5

The binary representation of 54 is 110110.
After flipping the third bit from the left, we get consecutive 5 bits. i.e. 111110.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 1000
2 <= N <= 10^9

Where 'N' is the integer that is to be looked into for the maximum consecutive ones after flipping 1 bit.

Time limit: 1 second
Sample Input 1:
3
1775         
12         
15
Sample Output 1:
8
3
4
4
Explanation For Sample Input 1:
For first test case:
The binary representation of 1775 is 11011101111.
After flipping the highlighted bit, we get consecutive 8 bits. (11011111111)

For second test case:
The binary representation of 12 is 1100.
After flipping the highlighted bit, we get consecutive 3 bits. (1110)

For third test case:
The binary representation of 15 is 1111.
There is no need to flip bits here since all bits are ones.
Sample Input 2:
2
71
54
Sample Output 2:
4
5
Explanation For Sample Input 2:
For first test case:
The binary representation of 71 is 1000111.
After flipping the 4th bit, we get consecutive 4 bits.

For second test case:
The binary representation of 54 is 110110.
After flipping the 3rd bit, we get consecutive 5 bits.
'''

def flipBit(a):
    s = ''
    while a:
        s = str(a & 1) + s
        a >>= 1
    
    res = 0 
    n = len(s)
    for i in range(n):
        l = i - 1
        r = i + 1
        while l >= 0 and s[l] == '1':
            l -= 1
        while r < n and s[r] == '1':
            r += 1
        res = max(res, r - l - 1)
    return res

#Sliding Window
def flipBit(a):
    s = ''
    while a:
        s = str(a & 1) + s
        a >>= 1
    
    res = 0 
    n = len(s)
    zerocnt = 0
    l = 0
    for r in range(n):
        zerocnt += 1 if s[r] == '0' else 0
        while zerocnt >= 2:
            if s[l] == '0':
                zerocnt -= 1
            l += 1
        res = max(res, r - l + 1)
    
    return res
