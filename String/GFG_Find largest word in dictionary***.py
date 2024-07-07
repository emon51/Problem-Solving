
'''
Given a string s and a string dictionary d, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Examples :

Input: d = {"ale", "apple", "monkey", "plea"}, s = "abpcplea"
Output: "apple" 
Explanation: After deleting "b", "c", "a" S became "apple" which is present in d.
Input: d = {"a", "b", "c"}, s = "abpcplea"
Output: "a"
Explanation: After deleting "b", "p", "c", "p", "l", "e", "a" S became "a" which is present in d.
Expected Time Complexity: O(n*x)
Expected Auxiliary Space: O(x) where x is the length of the string in d.

Constraints:
1 ≤ n,x ≤ 103
'''


class Solution:
    def findLongestWord (self, s, d):
        
        def got(p, q): #Checking p is a subsequence of q or not?
            i = j = 0 
            while i < len(p) and j < len(q):
                if p[i] == q[j]:
                    i += 1
                j += 1
            return i == len(p)
      
        arr = []
        for w in d:
            if got(w, s):
                arr.append(w)

      
        arr.sort()
        
        res = ''
        for w in arr:
            if len(res) < len(w):
                res = w
        return res
