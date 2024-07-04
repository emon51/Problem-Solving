
'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''
#Brute Force 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n = len(s)
        for i in range(n):
            pmap = Counter(p)
            for j in range(i, n):
                if s[j] not in pmap:
                    break 
                pmap[s[j]] -= 1
                if pmap[s[j]] == 0:
                    del pmap[s[j]]
            if not pmap:
                res.append(i)
        return  res
        
#Sliding Window(Fixed_size)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s) < len(p):
            return []
            
        p_window, s_window = {}, {}
        for i in range(len(p)):
            p_window[p[i]] = p_window.get(p[i], 0) + 1
            s_window[s[i]] = s_window.get(s[i], 0) + 1

        res = [0] if s_window == p_window else []
        l = 0
        for ch in s[len(p):]:
            s_window[s[l]] -= 1
            if s_window[s[l]] == 0:
                del s_window[s[l]]
            s_window[ch] = s_window.get(ch, 0) + 1
            if s_window == p_window:
                res.append(l + 1)
            l += 1
        return res



        
