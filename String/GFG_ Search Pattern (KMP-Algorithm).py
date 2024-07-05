
"""
Given two strings, one is a text string and other is a pattern string. The task is to print the indexes of all the occurences of pattern string in the text string. For printing, Starting Index of a string should be taken as 1. The strings will only contain lowercase English alphabets ('a' to 'z').

Example 1:

Input: 
text = "birthdayboy"
pattern = "birth"
Output: 
[1]
Explanation: 
The string "birth" occurs at index 1 in text.
Example 2:

Input:
text = "geeksforgeeks"
pattern = "geek"
Output: 
[1, 9]
Explanation: 
The string "geek" occurs twice in text, one starts are index 1 and the other at index 9.
Your Task:
You don't need to read input or print anything. Your task is to complete the function search() which takes the string text and the string pattern as input and returns an array denoting the start indices (1-based) of substring pattern in the string text. 

Expected Time Complexity: O(|text| + |pattern|).
Expected Auxiliary Space: O(1).

Constraints:
1<=|text|<=5*105
1<=|pattern|<=|text|
"""

#Brute-Forces(Accepted)
class Solution:
    def search(self, pattern, text):
        
        res = []
        patLen, textLen = len(pattern), len(text)
        
        for i in range(textLen - patLen + 1):
            j = 0
            while j < patLen and pattern[j] == text[i + j]:
                j += 1
            
            if j == patLen:
                res.append(i + 1)
        return res


#Accepted -------> string.find(value, start, end)
class Solution:
    def search(self, pat, txt):
        
        res = []
        i = txt.find(pat)
        if i == -1:
            return [-1]
        res.append(i + 1)
        while i != -1:
            i = txt.find(pat, i + 1)
            if i != -1:
                res.append(i + 1)
        return res
