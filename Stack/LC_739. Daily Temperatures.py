class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(temps)
        for i, temp in enumerate(temps):
            while stack and temp > stack[-1][1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, temp])
            
        while stack:
            res[stack[-1][0]] = 0
            stack.pop()
        return res
                
        
