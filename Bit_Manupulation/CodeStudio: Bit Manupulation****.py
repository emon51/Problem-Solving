
'''
Problem statement
You have a 32-bit unsigned integer called 'num' and another integer called 'i'.



You need to perform the following operations on the 'num' integer based on the value of 'i':



1. Get the bit value at the "i"th position of "num".

2. Set the bit at the "i"th position of "num".

3. Clear the bit at the "i"th position of "num".



We are starting bits from 1 instead of 0. (1-based)



For Example:
N=25  i=3
Output : 0 29 25

Bit at the 3rd position from LSB is 0. (1 1 0 0 1)

The value of the given number after setting the 3rd bit is 29. (1 1 1 0 1)

The value of the given number after clearing the 3rd bit is 25. (1 1 0 0 1)
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
9 3
Sample Output 1:
0 13 9
Explanation Of Sample Input 1:
Bit at the 3rd position from LSB is 0. ( 1 0 0 1)

The value of the given number after setting the 3rd bit is 13. ( 1 1 0 1)

The value of the given number after clearing the 3rd bit is 9. (1 0 0 1)
Sample Input 2:
11 2
Sample Output 2:
1 11 9
Explanation Of Sample Input 2:
The 2nd position from LSB is 1. (1 0 1 1)

The value of the given number after setting the 2nd bit is 11. (1 0 1 1)

The value of the given number after clearing the 2nd bit is 9. (1 0 0 1)
Constraints:
0 <= num <= 10^9
1 <= i <= 32
Time Limit: 1 sec
Follow Up:
Can you solve this in O(1) time?
'''


def bitManipulation(num : int, i : int) -> List[int]:
    
    res = []

    ithbit = num >> (i - 1) & 1
    new1 = num | (1 << (i - 1))
    new2 = num & ~(1 << (i - 1))

    res += [ithbit, new1, new2]

    return res
