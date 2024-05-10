#Problem: Search an element from sorted infinite array.



def solve(arr, target):
    
    def _binarySearch(arr, target, l, h):
        
        while l <= h:
            mid = (l + h) // 2
            if arr[mid] == target:
                return mid 
            elif arr[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return -1
        
        
        
    l, h = 0, 1
    while arr[h] < target:
        l = h 
        h = 2 * h 
    return _binarySearch(arr, target, l, h)
    

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    target = 11
    res = solve(arr, target)
    print(res)
