class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res = []
        
        l, r = 0, len(nums)-1
        first_pos = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                first_pos = mid
                r = mid -1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        
        l, r = 0, len(nums)-1
        last_pos = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                last_pos = mid
                l = mid +1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        res.append(first_pos)
        res.append(last_pos)
        return res
