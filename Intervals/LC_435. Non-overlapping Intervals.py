#Using stack.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() #sorted the intervals corresponding to the 1st value then 2nd value in ascending order.
        #print(intervals)
        res = 0 
        stack = []
        for s, e in intervals:
            if stack and stack[-1][1] > s:
                res += 1
                prev_s, prev_e = stack.pop()
                newInterval = [min(prev_s, s), min(prev_e, e)]
                stack.append(newInterval)
            else:
                stack.append([s, e])
                
        return res
