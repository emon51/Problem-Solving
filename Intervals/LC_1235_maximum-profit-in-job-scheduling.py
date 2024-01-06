#TLE
class Solution:
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:

        def fun(jobs, i, n, prev = -1):
            if i >= n:
                return 0
            #pick
            pick = 0
            if prev == -1 or jobs[prev][1] <= jobs[i][0]:
                pick = jobs[i][2] + fun(jobs, i + 1, n, i)
            #notPick
            notPick = fun(jobs, i + 1, n, prev)
            return max(pick, notPick)



        jobs = []
        for s, e, p in zip(start, end, profit):
           jobs.append([s, e, p])

        jobs.sort(key = lambda c: c[1])
        print(jobs)
        res = fun(jobs, 0, len(start))

        return res
#===============================================================================#
#MLE
class Solution:
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:

        def fun(jobs, i, n, prev = -1, memo = {}):

            if i >= n:
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            #pick
            pick = 0
            if prev == -1 or jobs[prev][1] <= jobs[i][0]:
                pick = jobs[i][2] + fun(jobs, i + 1, n, i, memo)
            #notPick
            notPick = fun(jobs, i + 1, n, prev, memo)
            val = max(pick, notPick)
            memo[(i, prev)] = val 
            return val



        jobs = []
        for s, e, p in zip(start, end, profit):
           jobs.append([s, e, p])

        jobs.sort(key = lambda c: c[1])
        print(jobs)
        res = fun(jobs, 0, len(start))

        return res
#===============================================================================#
