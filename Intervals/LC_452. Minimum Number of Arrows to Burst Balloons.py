
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        stack = []
        points.sort()
        for s, e in points:
            if stack and s <= stack[-1][1]:
                prev_s, prev_e = stack.pop()
                stack.append([max(prev_s, s), min(prev_e, e)])
            else:
                stack.append([s, e])
        
        return len(stack)

        
