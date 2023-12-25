"""
If we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

Find the sum of all the multiples of  or  below .

"""
#TLE
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res = 0
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            res += i
    print(res)
"""

"""
#Accepted
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res = 0
    
    k = (n - 1) // 3
    res += (3*k*(k+1))//2
    
    k = (n - 1) // 5
    res += (5*k*(k + 1)) // 2
    
    k = (n - 1) // 15
    res -= (15*k*(k + 1)) // 2
    print(res)

"""
Explanations:
k = (n - 1) // 3: Calculates the number of multiples of 3 below n (excluding n). Similarly, the next two lines calculate the number of multiples of 5 and 15.

answer += 3 * k * (k + 1) // 2: Adds the sum of multiples of 3 below n to the answer using the formula for the sum of an arithmetic series.

answer += 5 * k * (k + 1) // 2: Adds the sum of multiples of 5 below n to the answer using the same formula.

answer -= 15 * k * (k + 1) // 2: Since multiples of 15 (common multiples of 3 and 5) are added twice (once in multiples of 3 and once in multiples of 5), subtracts the sum of multiples of 15 below n to avoid double counting.
"""
