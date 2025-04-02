'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        #stored last_occurrences of character
        mapp = {}
        for i, ch in enumerate(s):
            mapp[ch] = i 
        
        n, start, end = len(s), 0, 0
        res = []
        for i in range(n):
            end = max(end, mapp[s[i]])
            if i == end:
                res.append(end  - start + 1)
                start = i + 1

        return res 

        
