'''
Problem statement
You have been given an integer ‘N’. You need to print an inverted isosceles triangle of stars such that the height of the triangle is N.

For example :
If N = 4 then the output will
*******
 *****
  ***
   *
'''


def Triangle(n):
    space = 0
    res = []
    for r in range(n, 0, -1):
        s = ''
        for _ in range(space):
            s += ' '
        for c in range(2 * r - 1):
            s += '*'
        res.append(s)
        space += 1
    
    return res

