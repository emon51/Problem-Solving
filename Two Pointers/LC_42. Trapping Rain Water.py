
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

#Brute Force 
class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0 
        n = len(height)
        for i in range(n):
            l = i - 1
            r = i + 1
            leftmaxht = 0
            rightmaxht = 0
            while l >= 0:
                leftmaxht = max(leftmaxht, height[l])
                l -= 1
            while r < n:
                rightmaxht = max(rightmaxht, height[r])
                r += 1
            water = min(leftmaxht, rightmaxht) - height[i]
            res += water if water > 0 else 0
        
        return res
            
            


#Optimal
class Solution:
    def trap(self, height: List[int]) -> int:

        prevmaxht = []
        postmaxht = []

        for i, ht in enumerate(height):
            if i == 0:
                prevmaxht.append(ht)
            else:
                prevmaxht.append(max(prevmaxht[-1], ht))

        for i, ht in enumerate(height[::-1]):
            if i == 0:
                postmaxht.append(ht)
            else:
                postmaxht.append(max(postmaxht[-1], ht))
        postmaxht = postmaxht[::-1]

        res = 0 
        for i, ht in enumerate(height):
            water = min(prevmaxht[i], postmaxht[i]) - ht
            res += water if water > 0 else 0
        return res

        
        
