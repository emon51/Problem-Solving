class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, (s, e) in enumerate(intervals):
            if newInterval[1] < s:
                res.append(newInterval)
                return res + intervals[i:]
            elif e < newInterval[0]:
                res.append([s, e])
            #overlap
            else:
                #update new interval
                newInterval = [min(s, newInterval[0]), max(e, newInterval[1])]
        res.append(newInterval)
        return res
        
        
       
  
        
