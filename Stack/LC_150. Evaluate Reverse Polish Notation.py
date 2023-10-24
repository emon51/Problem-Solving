class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for val in tokens:
            if val not in "+-*/":
                stack.append(int(val))
            else:
                a = stack.pop()
                b = stack.pop()
                if val == "+":
                    stack.append(a + b)
                elif val == "-":
                    stack.append(b - a)
                elif val == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(b/a))
        return stack[0]
