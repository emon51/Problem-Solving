class Solution:
    def minOperations(self, nums: List[int]) -> int:

        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        res = 0 
        for key, freq in d.items():
            if freq < 2:
                return -1
            res += math.ceil(freq / 3)
        
        return res
