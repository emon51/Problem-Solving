#Using stack.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda c: c[0], reverse = False)
        stack = []
        for s, e in intervals:
            if stack and stack[-1][1] >= s:
                prev_s, prev_e = stack.pop()
                newInterval = [min(prev_s, s), max(prev_e, e)]
                stack.append(newInterval)
            else:
                stack.append([s, e])
        return stack
        
