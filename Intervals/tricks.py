
If [s1, e1] and [s2, e2] are two closed intervals then

1. They are not overlap/intersect if: (e1 < s2 or e2 < s1)
2. They are overlap/intersect if: not (e1 < s2 or e2 < s1)


'''
Problem statement
You have been given two sorted arrays/lists of closed intervals ‘INTERVAL1’ and ‘INTERVAL2’. A closed interval [x, y] with x < y denotes the set of real numbers ‘z’ with x <= z <= y.

Now, your task is to find the intersection of these two interval lists.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [0, 2] and [1, 3] is [1, 2].


Note :

1. Each list of intervals is pairwise disjoint.
2. 'INTERVAL1' and 'INTERVAL2' don't contain duplicate intervals.
3. If there is no intersection present in 'INTERVAL1' and 'INTERVAL2' return an empty array/list.
For example, if INTERVAL1 = [[0, 5], [7, 9], [10, 11]] and INTERVAL2 = [[0, 2], [3, 7], [12, 15]], then the intersection array/list will be [[0, 2], [3, 5], [7, 7]].

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 100
0 <= N1 <= 5000
0 <= N2 <= 5000 
0 <= INTERVAL1[i][0] <=10^5
INTERVAL1[i][0] < INTERVAL1[i][1] <= 10^5
0 <= INTERVAL2[i][0] <=10^5
INTERVAL2[i][0] < INTERVAL2[i][1] <= 10^5

where 'T' denotes the number of test cases to be run, 'N1' and 'N2' denote the sizes of 'INTERVAL1' and 'INTERVAL2' respectively.

Time Limit: 1 second
Sample Input 1:
2
2 3
2 8 12 16
5 9 10 12 14 15
3 0
1 2 4 6 8 12
Sample output 1:
5 8 12 12 14 15
Explanation of Sample output 1:
For the first test case, INTERVAL1 is [[2, 8], [12, 16]] and INTERVAL2 is [[5, 9], [10, 12], [14, 15]] the intersections between INTERVAL1 and INTERVAL2 are [5 , 8], [12, 12] and [14, 15].
For the second test case, since there is no interval present in INTERVAL2 hence there is no intersection.
Sample Input 2:
2
2 2
2 4 8 10
5 7 11 14
1 1
2 4
2 4
Sample output 2:
2 4
'''

def intersectionIntervals(interval1, interval2, n1, n2):
    
    res = []
    i, j = 0, 0 
    while i < n1 and j < n2:
        s1, e1 = interval1[i]
        s2, e2 = interval2[j]
        #overlap
        if not (e1 < s2 or e2 < s1):
            s, e = max(s1, s2), min(e1, e2)
            res.append([s, e])
        if e2 < e1:
            j += 1
        else:
            i += 1
    
    return res
