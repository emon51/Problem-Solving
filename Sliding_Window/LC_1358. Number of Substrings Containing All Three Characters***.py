'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''

#Brute Force
class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        res = 0 
        for i in range(n):
            st = set()
            for j in range(i, n):
                st.add(s[j])
                if len(st) == 3:
                    res += 1
        return res
               
        
#Sliding Window
class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        res = 0
        mp = {}
        l = 0
        for r, ch in enumerate(s):
            mp[ch] = mp.get(ch, 0) + 1
            while len(mp) == 3:
                res += (n - r)
                mp[s[l]] -= 1
                if mp[s[l]] == 0:
                    del mp[s[l]]
                l += 1
        return res
               
        
