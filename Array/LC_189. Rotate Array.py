
#TLE
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Brute force, TC: O(n*k), SC: O(1)
        n = len(nums)
        
        for _ in range(k):
          tmp = nums[n-1] 
          for i in range(n-2, -1, -1):
            nums[i+1] = nums[i] 
          nums[0] = tmp
          
 
 #Accepted
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #TC: O(n), SC: O(k)
        n = len(nums)
        k %= n
        
        tmp_arr = []
        for i in range(n - k, n):
          tmp_arr.append(nums[i])
        
        for i in range(n-k -1, -1, -1):
          nums[i+k] = nums[i] 

        tmp_idx = 0 
        for i in range(k):
          nums[i] = tmp_arr[tmp_idx] 
          tmp_idx += 1 
          

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def _reverse(arr, s, e):
          while s < e:
            arr[s], arr[e] = arr[e], arr[s]
            s, e = s + 1, e - 1
          
        #TC: O(n), SC: O(1)
        n = len(nums)
        k %= n
        
        _reverse(nums, 0, n - k-1) 
        _reverse(nums, n - k, n-1) 
        _reverse(nums, 0, n - 1)
          
          
#Follow up question: left rotation, coding ninjas 
          
            
        
        
        
        
