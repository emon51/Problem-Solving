
'''
Given a string S of opening and closing brackets '(' and ')' only. The task is to find an equal point. An equal point is an index such that the number of closing brackets on right from that point must be equal to number of opening brackets before that point.


Example 1:

Input: str = "(())))("
Output: 4
Explanation:
After index 4, string splits into (())
and ))(. Number of opening brackets in the
first part is equal to number of closing
brackets in the second part.
Example 2:
Input : str = "))"
Output: 2
Explanation:
As after 2nd position i.e. )) and "empty"
string will be split into these two parts:
So, in this number of opening brackets i.e.
0 in the first part is equal to number of
closing brackets in the second part i.e.
also 0.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function findIndex() which takes the string S as inputs and returns the occurrence of the equal point in the string.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ S ≤ 106
String can be unbalanced
'''

#Brute Force(TLE)

class Solution:
    def findIndex(self, s): 
        
        n = len(s)
        for i in range(n + 1):
            openn = close = 0 
            a, b = i - 1, i
            while a >= 0:
                openn += 1 if s[a] == '(' else 0 
                a -= 1
            while b < n:
                close += 1 if s[b] == ')' else 0 
                b += 1
            
            if openn == close:
                return  i
        return -1


#Optimal (Greedy)

class Solution:
    def findIndex(self,s):
        res = 0
        for i in range(len(s)):
            if s[i]==')':
                res += 1
        return res





















