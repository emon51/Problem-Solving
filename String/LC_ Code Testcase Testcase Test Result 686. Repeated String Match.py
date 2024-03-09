
"""
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

 

Example 1:

Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
Example 2:

Input: a = "a", b = "aa"
Output: 2
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist of lowercase English letters.
"""

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        if b in a:
            return 1

        map_a, map_b = Counter(a), Counter(b)
        for b_ch in map_b.keys():
            if b_ch not in map_a:
                return -1
        temp_a = a
        cnt = 1

        while len(a) < len(b):
            a += temp_a
            cnt += 1
        
        if b in a:
            return cnt
        
        a += temp_a

        if b in a:
            return cnt + 1

        return -1
        
        
