
'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
'''

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


#Space Optimiztion
#We have to track just previous ending point.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        prev_end = intervals[0][1]
        res = 0
        for s, e in intervals[1: ]:
            if s < prev_end:
                res += 1
                prev_end = min(prev_end, e)
            else:
                prev_end = e
        return res
        
