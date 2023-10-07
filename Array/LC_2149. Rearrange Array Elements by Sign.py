#01
#TC: O(n), SC: O(n + n/2 + n/2) = O(2n)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n, res, positives, negatives = len(nums), [], [], []
        
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
                
        for i in range(len(positives)):
            res.append(positives[i])
            res.append(negatives[i])
        return res


#02
#TC: O(n); SC: O(n)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        #All the positives element will be placed at even index and negative element at odd index.
        n = len(nums); res = [-1] * n 
        
        posi, negi = 0, 1
        for num in nums:
            if num < 0:
                res[negi] = num
                negi += 2
            else:
                res[posi] = num
                posi += 2
        return res
        
