
'''
Description
A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).

You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.

Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.

 

Example 1:



Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
Example 2:



Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
Example 3:

Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
Output: [[-5,-4],[-3,-2],[4,5],[8,9]]
 

Constraints:

1 <= intervals.length <= 104
-109 <= ai < bi <= 109
'''

#Solution 1
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        a, b = toBeRemoved
        ans = []
        for s, e in intervals:
            #No Overlap
            if s >= b or e <= a:
                ans.append([s, e])
            #Overlap
            elif s < a and b < e:
                ans.append([s, a])
                ans.append([b, e])
            elif s < a: 
                ans.append([s, a])
            elif e > b:  
                ans.append([b, e])
         return ans


#Solution 2
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        a, b = toBeRemoved
        ans = []
        for s, e in intervals:
            #No Overlap
            if s >= b or e <= a:
                ans.append([s, e])
            else:
                #Overlap
                if s < a: # Partial intersection at the start
                    ans.append([s, a])
                if e > b: # Partial intersection at the end
                    ans.append([b, e])
        return ans


#Same Question: https://www.naukri.com/code360/problems/remove-interval_1380268?leftPanelTabValue=PROBLEM







