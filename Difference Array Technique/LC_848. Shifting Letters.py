
Problem link: https://leetcode.com/problems/shifting-letters/

#Brute Force 
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        arr = [ch for ch in s]
        for i in range(len(s)):
            for j in range(i + 1):
                orginal = ord(arr[j]) - ord('a')
                code = (orginal + shifts[i]) % 26
                arr[j] = chr(code + ord('a'))
        return ''.join(arr)


#Optimal 
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        arr = [0 for _ in s]
        for i in range(len(s)):
            arr[0] += shifts[i]
            if (i + 1) < len(s):
                arr[i + 1] -= shifts[i] 
        
        for i in range(1, len(s)):
            arr[i] += arr[i - 1]
        
        for i in range(len(s)):
            shift = arr[i] % 26 
            orginal = ord(s[i]) - ord('a')
            code = (orginal + shift) % 26
            arr[i] = chr(code + ord('a'))           
        return ''.join(arr)
        
