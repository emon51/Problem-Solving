class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "}": "{", "]": "["}
        
        stack = []
        for val in s:
            if stack and val in d and stack[-1] == d[val]:
                stack.pop()
            else:
                stack.append(val)
            
        return stack == []
