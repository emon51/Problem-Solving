'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i, j = len(a) - 1, len(b) - 1
        carry = 0 
        res = []
        while i >= 0 or j >= 0 or carry:
            A = int(a[i]) if i >= 0 else 0 
            B = int(b[j]) if j >= 0 else 0 
            sm = A + B + carry 
            carry = (sm // 2)
            res.append(sm % 2)
            i -= 1
            j -= 1
        
        return ''.join(map(str, res[:: -1]))


#Similar Problem: From SuperCoder: Add Two Numbers Represented as Character Arrays

'''
Given two numbers represented as arrays of characters in decimal format, add them and return the result in the same format.

Write a function that takes two-character arrays representing two non-negative integers and returns a character array representing their sum.



Example 1:

Input: nums1 = ['1', '2', '3'] , nums2 =  ['4', '5', '6'] 
Output: ['5', '7', '9']
Explanation: Adding each corresponding pair of digits:
1 + 4 = 5
2 + 5 = 7
3 + 6 = 9


Example 2:

Input: nums1 = ['9', '9', '9'], nums2 = ['1']
Output: ['1', '0', '0', '0']
Explanation: Adding the numbers represented by the arrays:
999 + 1 = 1000

Constraints

The input character arrays will only contain digits ('0'-'9').
The input character arrays will not have leading zeros unless the number is 0 itself.
The length of the input arrays will be between 1 and 10^4.
'''

def addCharacterArrays(nums1, nums2):
    res = []
    i, j = len(nums1) - 1, len(nums2) - 1
    carry = 0 
    while i >= 0 or j >= 0 or carry > 0:
        a = int(nums1[i]) if i >= 0 else 0 
        b = int(nums2[j]) if j >= 0 else 0 
        sm = a + b + carry 
        carry = (sm // 10)
        res.append(str(sm % 10))
        i -= 1
        j -= 1
    
    return res[:: -1]

print(addCharacterArrays(['1', '2', '3'], ['4', '5', '6'])) # Output: ['5', '7', '9']
