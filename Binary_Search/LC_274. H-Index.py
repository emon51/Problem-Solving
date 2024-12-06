
'''
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 

Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
'''

#Brute Force(Linear Search)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = 0
        for h in range(1, max(citations) + 1):
            count = 0 
            for noc in citations:
                count += 1 if h <= noc else 0 
            if h <= count:
                res = h 
        return res 


#Optimal(Binary Search)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = 0
        l, r = 1, max(citations)
        while l <= r:
            mid = l + (r - l) // 2
            count = 0 
            for noc in citations:
                count += 1 if mid <= noc else 0 
            if mid <= count:
                res = mid 
                l = mid + 1
            else:
                r = mid - 1
        return res 


        
