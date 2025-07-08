
Problem link: https://leetcode.com/problems/range-sum-query-mutable/description/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.ST = [0] * (4 * self.n) #segement tree
        self.construct_tree(0, 0, self.n - 1) #segment_tree's_index, lower_bound, upper_bound
    
    def construct_tree(self, i, l, r):
        if l == r:
            self.ST[i] = self.nums[r]
            return self.ST[i]
        mid = l + (r - l) // 2 
        lt = self.construct_tree(2 * i + 1, l, mid)
        rt = self.construct_tree(2 * i + 2, mid + 1, r)
        self.ST[i] = (lt + rt)
        return self.ST[i]
        

    def update(self, index: int, val: int) -> None:
        #self.nums[index] = val
        def change(i, l, r):
            if l == r == index:
                self.ST[i] = val 
                return 
            if index < l or index > r:
                return
            mid = l + (r - l) // 2
            lt = change(2 * i + 1, l, mid)
            rt = change(2 * i + 2, mid + 1, r)
            self.ST[i] = self.ST[2 * i + 1] + self.ST[2 * i + 2]
            return self.ST[i]

        change(0, 0, self.n - 1)
        

    def sumRange(self, left: int, right: int) -> int:

        def calculate(i, l, r):
            #[l, r] out of [left, right]
            if r < left or right < l:
                return 0 
            #[l, r] completely intersect within [left, right]
            if left <= l and r <= right:
                return self.ST[i]
            #[l, r] partially intersect within [left, right]
            mid = l + (r - l) // 2
            lt = calculate(2 * i + 1, l, mid)
            rt = calculate(2 * i + 2, mid + 1, r)
            return (lt + rt)
        
        return calculate(0, 0, self.n - 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
