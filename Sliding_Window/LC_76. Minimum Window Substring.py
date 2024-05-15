'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

#Brute Force 1
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        prev_len = float("inf")
        res = ""
        for i in range(len(s)):
            d = Counter(t)
            for j in range(i, len(s)):
                if s[j] in d:
                    d[s[j]] -= 1
                    if d[s[j]] == 0:
                        del d[s[j]]
                if not d:
                    if (j - i + 1) < prev_len:
                        res = s[i:j + 1]
                        prev_len = j - i + 1
        return res

#Brute Force 2
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = Counter(t)
        res = ''
        maxlen = float('inf')
        for i in range(len(s)):
            mp = tmap.copy()
            for j in range(i, len(s)):
                if s[j] in mp:
                    mp[s[j]] -= 1
                    if mp[s[j]] == 0:
                        del mp[s[j]]
                if not mp and (j - i + 1) < maxlen:
                    res = s[i: j + 1]
                    maxlen = j - i + 1
                    
        return res

                    

        

#Accepted

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tcount = Counter(t)
        window = {}
        minlen = float('inf')
        res = ''
        reqcount, currcount = len(tcount), 0
        l = 0

        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in tcount and window[ch] == tcount[ch]:
                currcount += 1
            
            while currcount == reqcount:
                if (r - l + 1) < minlen:
                    minlen = (r - l + 1)
                    res = s[l: r + 1]
                
                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    currcount -= 1
                l += 1
        return res
                
