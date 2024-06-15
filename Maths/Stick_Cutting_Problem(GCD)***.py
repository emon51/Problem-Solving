
'''
Mr.Chow just got back home from a long trip in Bangkok. He went into his kitchen to make some noodles but was surprised to find everything messed up.

"The Wolfpack must have done this". Now as we all know Mr. Chow isn't much of a cleanliness freak, but one thing that was bothering him the most was that his noodle sticks were all broken. He decides to do something about this.

Now, there are N sticks. Given the length of each stick, Mr.Chow wants to cut the sticks such that they all become of equal lengths and no segment of any stick is wasted. Also Mr.Chow wants the resulting sticks to be as long as possible. Let this resulting length be x.

He begins with the task but keeps on failing. Hangover you see! So he calls you up and asks for help.

Note: The lengths have to be integers. So make the cuts on integral points only.

INPUT

The first line contains T no of test cases. Each test case begins with a single integer N - number of sticks. Then there are N integers in the next line, ith integer being the length of the ith stick.

OUTPUT

You have to print the answer of each test case, x in a separate line.

CONSTRAINTS

1<=T<=200

1<=N<=1000

1<=length<=230

Time Limit: 2 sec

EXAMPLE

INPUT

2

3

4 6 8

4

3 2 5 7

OUTPUT

2

1

Explanation

For the first case, we have 3 sticks (each '-' denotes a unit length of noodle stick).

---- , ------ , --------

We chop them in size of 2 each

-- -- , -- -- -- , -- -- -- --

So we have 9 sticks of length 2 each, i.e. x=2 and no segment is wasted, also 2 is the maximum length that we can achieve. We cant break the sticks into size of 3 because that will lead to

--- - , --- --- , --- --- --

The resulting sticks now have lengths 3, 1, 3, 3, 3, 3, 2 (not same).
'''


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(arr, n):
    res = arr[0]
    for num in arr[1:]:
        res = gcd(res, num)
    return res
        
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        res = solve(arr, n)
        print(res)
