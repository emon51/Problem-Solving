
Problem link: https://leetcode.com/problems/shifting-letters-ii/description/


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        arr = [0] * n
        for si, ei, direction in shifts:
            val = 1 if direction == 1 else -1
            arr[si] += val
            if ei + 1 < n:
                arr[ei + 1] -= val

        for i in range(1, n):
            arr[i] += arr[i - 1]

        
        for i in range(n):
            shift = (arr[i] + 26) % 26  #Wrapped up positive and Negative value.
            original = ord(s[i]) - ord('a')
            shifted = (original + shift) % 26
            arr[i] = chr(shifted + ord('a'))

        return ''.join(arr)
