class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        
        #TC: m*log(n)
        def  _bs(l, r, arr, tar):
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == tar:
                    return True  
                elif arr[mid] < tar:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        
        m, n = len(mat), len(mat[0])
        for r in range(m):
            if _bs(0, n-1, mat[r], target):
                return True 
        return False
#========================================================================================#
class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        
        #TC: log(m*n)
        def  _bs(l, r, arr, tar): #binary_search.
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == tar:
                    return True  
                elif arr[mid] < tar:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        
        m, n = len(mat), len(mat[0])
        ur, br = 0, m-1 #up_row, bottom_row
        while ur <= br:
            mid = ur + (br - ur) // 2
            if mat[mid][0] <= target <= mat[mid][n-1]:
                if _bs(0, n-1, mat[mid], target):
                    return True 
                return False
            
            elif mat[mid][0] < target:
                ur = mid + 1
            else:
                br = mid - 1
        return False
