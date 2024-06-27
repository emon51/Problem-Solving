
#Binary Search 
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
        res = 0 
        low, high = 1, position[-1] - position[0]
        while low <= high:
            mid = low + (high - low) // 2
            l = 0 
            cnt = 1
            for r in range(1, len(position)):
                if abs(position[l] - position[r]) >= mid:
                    cnt += 1
                    l = r 
            if m <= cnt:
                res = max(res, mid)
                low = mid + 1
            else:
                high = mid - 1
        return res

        
