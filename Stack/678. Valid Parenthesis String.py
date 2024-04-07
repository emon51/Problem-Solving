'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
'''

#Recursion
class Solution:
    def checkValidString(self, s: str) -> bool:

        def fun(i, n, open = 0):
            if i == n:
                return open == 0
            res = False
            if s[i] == '(':
                res = res or fun(i + 1, n, open + 1)
            elif s[i] == ')' and open > 0:
                res = res or fun(i + 1, n, open - 1)
            elif s[i] == '*':
                res = res or fun(i + 1, n, open)            # * -> ''
                if open > 0:
                    res = res or fun(i + 1, n, open - 1)    # * -> )
                res = res or fun(i + 1, n, open + 1)        # * -> (
            return res

        return fun(0, len(s))
#=====================================================================================================#

#Recursion with memoization
class Solution:
    def checkValidString(self, s: str) -> bool:

        def fun(i, n, open = 0, dp = {}):
            if (i, open) in dp:
                return dp[(i, open)]
            if i == n:
                return open == 0
            res = False
            if s[i] == '(':
                res = res or fun(i + 1, n, open + 1)
            elif s[i] == ')' and open > 0:
                res = res or fun(i + 1, n, open - 1)
            elif s[i] == '*':
                res = res or fun(i + 1, n, open)            # * -> ''
                if open > 0:
                    res = res or fun(i + 1, n, open - 1)    # * -> )
                res = res or fun(i + 1, n, open + 1)        # * -> (
            val = res
            dp[(i, open)] = val 
            return val

        return fun(0, len(s))
#========================================================================================================#
#Stack
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        s1, s2 = [], []
        for i, ch in enumerate(s):
            if ch == '(':
                s1.append(i)
            elif ch == '*':
                s2.append(i)
            else:
                if s1:
                    s1.pop()
                elif s2:
                    s2.pop()
                else:
                    return False
        while s1 and s2 and s1[-1] < s2[-1]:
            s1.pop()
            s2.pop()
        return s1 == []
        
            
