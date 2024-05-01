
'''
You are playing a game with integers. You start with the integer 1 and you want to reach the integer target.

In one move, you can either:

Increment the current integer by one (i.e., x = x + 1).
Double the current integer (i.e., x = 2 * x).
You can use the increment operation any number of times, however, you can only use the double operation at most maxDoubles times.

Given the two integers target and maxDoubles, return the minimum number of moves needed to reach target starting with 1.

 

Example 1:

Input: target = 5, maxDoubles = 0
Output: 4
Explanation: Keep incrementing by 1 until you reach target.
Example 2:

Input: target = 19, maxDoubles = 2
Output: 7
Explanation: Initially, x = 1
Increment 3 times so x = 4
Double once so x = 8
Increment once so x = 9
Double again so x = 18
Increment once so x = 19
Example 3:

Input: target = 10, maxDoubles = 4
Output: 4
Explanation: Initially, x = 1
Increment once so x = 2
Double once so x = 4
Increment once so x = 5
Double again so x = 10
 

Constraints:

1 <= target <= 109
0 <= maxDoubles <= 100

'''
#TLE
class Solution:
    def minMoves(self, target: int, d: int) -> int:

        #src, double_option
        def fun(num, d):
            if num == target:
                return 0
            if num > target:
                return float('inf')
            
            f2 = float('inf')
            f1 = 1 + fun(num + 1, d)
            if d > 0:
                f2 = 1 + fun(2 * num, d - 1)
            
            return min(f1, f2)
        
        return fun(1, d)


#Greedy

class Solution:
    def minMoves(self, target: int, d: int) -> int:

        move = 0 
        while target > 1:
            if target % 2 == 0 and d > 0:
                target //= 2
                d -= 1
                move += 1
            elif d == 0:
                move += (target - 1)
                break 
            else:
                target -= 1
                move += 1
        return move
        
