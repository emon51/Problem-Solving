

'''
There is a string, s of lowercase English letters that is repeated infinitely many times. Given an integer, n, find and print the number of letter a's in the first n  letters of the infinite string.

s = abcac 
n = 10

The substring we consider is abcacabcac , the first 10 characters of the infinite string. There are 4 occurrences of a in the substring. so output: 4
'''

#Optimal
def repeatedString(s, n):
    
    x = 0 #frequency of 'a' in the main string, s.
    for ch in s:
        x += 1 if ch == 'a' else 0 
    res = x * (n // len(s))
    
    for ch in s[: n % len(s)]:
        res += 1 if ch == 'a' else 0
    
    return res 
    
