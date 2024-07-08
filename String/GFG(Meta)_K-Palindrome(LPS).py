
'''
A string is k palindrome if it can be transformed into a palindrome on removing at most k characters from it. Your task is to complete the function is_k_palin which takes two arguments a string str and a number N . Your function should return true if the string is k palindrome else it should return false.

Input:
The first line of input is an integer T denoting the number of test cases . Then T test cases follow . Each test case  contains a string str and an integer N separated by space.  

Output:
The output will be 1 if the string is  k palindrome else 0 .

Constraints:
1<=T<=100
1<=length of str<=100
1<=N<=20

Example:
Input
2
abcdecba 1
acdcb  1
Output
1
0

'''


#TLE

def is_k_palin(s, k):
    
    def lps(s, l, r):
        if l > r:
            return 0
        if l == r:
            return 1 
        a = b = c = 0
        if s[l] == s[r]:
            a = 2 + lps(s, l + 1, r - 1)
        else:
            b = lps(s, l + 1, r)
            c = lps(s, l, r - 1)
        return max(a, b, c)
       
            
    count = len(s) - lps(s, 0, len(s) - 1)
    return 1 if count <= k else 0


  #Accepted(Memoization)

  def is_k_palin(s, k):
    
    def lps(s, l, r, dp):
        if (l, r) in dp:
            return dp[(l, r)]
        if l > r:
            return 0
        if l == r:
            return 1 
        a = b = c = 0
        if s[l] == s[r]:
            a = 2 + lps(s, l + 1, r - 1, dp)
        else:
            b = lps(s, l + 1, r, dp)
            c = lps(s, l, r - 1, dp)
        val = max(a, b, c)
        dp[(l, r)] = val
        return val 
       
            
    count = len(s) - lps(s, 0, len(s) - 1, {})
    return 1 if count <= k else 0


#  ans = len(s)  - lps 
