'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
'''

#Brute Force 
#TC: O(N^3); SC: O(N)
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        def valid(ss):
            stack = []
            for ch in ss:
                if stack and ch == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(ch)
            return stack == []

        res = 0 
        for i in range(len(s)):
            for j in range(i, len(s)):
                if valid(s[i: j + 1]):
                    res = max(res, j - i + 1)
        return res         



#Optimal
#TC: O(N); SC: O(N) 
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []
        for i, ch in enumerate(s):
            if stack and s[stack[-1]] == '(' and ch == ')':
                stack.pop()
            else:
                stack.append(i)
        
        #print(stack)
        stack = [-1] + stack + [len(s)]        
        #print(stack)
        res = 0 
        for i in range(1, len(stack)):
            res = max(res, stack[i] - stack[i - 1] - 1)
        return res 
        

