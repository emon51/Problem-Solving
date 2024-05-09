
'''
Problem statement
You are given an array/list ‘BINARYNUMS’ that consists of ‘N’ distinct strings which represent all integers from 0 to N in binary representation except one integer. This integer between 0 to ‘N’ whose binary representation is not present in list ‘BINARYNUMS’ is called ‘Missing Integer’.

Your task is to find the binary representation of that ‘Missing Integer’. You should return a string that represents this ‘Missing Integer’ in binary without leading zeros.

Note

1. There will be no leading zeros in any string in the list ‘BINARYNUMS’.
Example:

Consider N = 5 and the list ‘binaryNums’=  [“0”, “01”, “010”, “100”, “101”].  This list consists of the binary representation of numbers [0, 1, 2, 4, 5]. Clearly, the missing number is 3 and its binary representation will be “11”. So you should return string “11”.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 50
1 <= N <= 10 ^ 4

Where ‘T’ is the total number of test cases and ‘N’ is the size of list ‘BINARYNUMS’

Time limit: 1 sec.
Sample Input 1:
2
1
1
5
0 01 010 100 101
Sample Output 1:
0
11
Explanation of Sample Input 1:
Test case 1:
There is only one string in ‘BINARYNUMS’ and that is “1”, which represents integer 1. Clearly, Missing Integer is 0, and its binary representation is also “0”.       

Test case 2:
See the problem statement for an explanation.
Sample Input 2:
2
3
0 10 11
8
0 1 10 11 100 101 110 111
Sample Output 2:
1
1000
'''


def findMissingNumber(arr, n):
    
    def binTodec(s):
        for i in range(len(s)):
            if s[i] == '1':
                break
        s = s[i: ]
        n = len(s)
        p = n - 1
        dec = 0
        for i in range(n):
            dec += int(s[i]) * 2 ** p 
            p -= 1
        return dec

    def decTobin(m):
        res = ''
        while m:
            res = str(m % 2) + res
            m //= 2
        return res if res else '0'

    for i in range(n):
        arr[i] = binTodec(arr[i])
    
    m = n * (n + 1) // 2 - sum(arr)
    #return bin(m)[2: ]

    return decTobin(m)
    
