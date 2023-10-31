#TLE
class Solution:
    def getSum(self, a: int, b: int) -> int:

        while b:
            sm = a ^ b 
            carry = (a & b) << 1
            a = sm 
            b = carry 
        return a
        
