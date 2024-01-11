"""
In order to get the smallest possible number, we have to get rid of as many as possible big digits in the
most significant places on the left. We can use a monotonically increasing stack to help us remove 
those big digits. When adding a new digit, 
we check whether the previous one is bigger than the current and pop it out. 
In the end, we concatenate the remaining elements from the stack and return the result.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        for n in num:
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
            if not stack and n == '0':
                continue
            stack.append(n)

        if k:
            stack = stack[: -k]
   
        return ''.join(stack) if stack else '0'
