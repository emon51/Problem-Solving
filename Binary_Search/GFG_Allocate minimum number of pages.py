
'''
You have n books, each with arr[i] number of pages. m students need to be allocated contiguous books, with each student getting at least one book.
Out of all the permutations, the goal is to find the permutation where the sum of maximum number of pages in a book allotted to a student should be minimum, out of all possible permutations.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).

 

Examples:

Input: n = 4, arr[] = {12,34,67,90}, m = 2
Output: 113
Explanation: Allocation can be done in following ways:
{12} and {34, 67, 90} Maximum Pages = 191
{12, 34} and {67, 90} Maximum Pages = 157
{12, 34, 67} and {90} Maximum Pages =113.
Therefore, the minimum of these cases is 113,
which is selected as the output.

Input: n = 3, arr[] = {15,17,20}, m = 2
Output: 32
Explanation: Allocation is done as {15,17} and {20}.

Expected Time Complexity: O(n logn)
Expected Auxilliary Space: O(1)


Constraints:
1 <=  n, m <= 105
1 <= arr[ i ] <= 106                                 

 
'''

#Linear Search 

class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,n ,arr ,m):
        
        if n < m:
            return -1
            
        for p1 in range(max(arr), sum(arr) + 1):
            stu = 1
            curr = 0 
            for p2 in arr:
                if (curr + p2) <= p1:
                    curr += p2 
                else:
                    stu += 1
                    curr = p2 
            if stu <= m:
                return p1
        return -1


#Binary Search 

class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,n ,arr ,m):
        
        if n < m:
            return -1
            
        l = max(arr)
        r = sum(arr)
        while l <= r:
            mid = l + (r - l) // 2 
            stu = 1
            curr = 0 
            for p2 in arr:
                if (curr + p2) <= mid:
                    curr += p2 
                else:
                    stu += 1
                    curr = p2 
            if stu <= m:
                r = mid - 1
            else:
                l = mid + 1
        return l
            
            















            
            














