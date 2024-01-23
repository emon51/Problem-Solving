"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
"""

"""
To solve this problem, we can use backtracking to generate all possible subsequences of the given array and check if each 
subsequence has unique characters. If a subsequence has unique characters, you can update the maximum length accordingly.
"""
"""
#Generating all subsequences
arr = [1, 2, 3]
def f(i,  p = []):
	print(p)
	for j in range(i, len(arr)):
		f(j + 1, p + [arr[j]])
		
f(0)
"""

#Solution_1
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s):
            return len(s) == len(set(s))

        def fun(i, p = ""):
            nonlocal res
            if i >= len(arr):
                if is_unique(p):
                    res = max(res, len(p))
                return 
            #pick
            fun(i + 1, p + arr[i])
            #not_pick
            fun(i + 1, p)

        res = 0
        fun(0)

#Solution_2
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s):
            return len(s) == len(set(s))

        def fun(i, p = ""):
           nonlocal res
           if is_unique(p):
               res = max(res, len(p))
           for j in range(i, len(arr)):
               fun(j + 1, p + arr[j])

        res = 0
        fun(0)
        return res


