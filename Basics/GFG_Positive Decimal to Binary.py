'''
Given a decimal number N, compute its binary equivalent.

Example 1:

Input: N = 7
Output: 111
 

Example 2:

Input: N = 33
Output: 100001
Your Task:
You don't need to read input. Complete the function toBinary() which takes the decimal number N as the input parameter and prints its binary equivalent.
Note: Print the output in a single line, the next line character is printed by the Driver Code.
'''


#Solution_1
#User function Template for python3
def toBinary(n):
    
    arr = []
    while n:
        arr.append(n % 2)
        n //= 2 
    
    res = 0 
    for digit in arr[:: -1]:
        res = res * 10 + digit 
    
    print(res)



#Solution_2
def toBinary(n):
    
    res = ''
    while n:
        res = str(n % 2) + res 
        n //= 2 
    
    print(res)








