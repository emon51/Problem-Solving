#User function Template for python

#TLE, TC: O(n+m), SC: O(n + m)__in worst case, if all element in 2 array are unique.
class Solution:    
    
    def findUnion(self,a,b,n,m):
        i, j = 0, 0 
        res = []
        while i < n and j < m:
            if a[i] < b[j]:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1 
            elif a[i] == b[j]:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
                j += 1 
            else:
                if not res or res[-1] != b[j]:
                    res.append(b[j])
                j += 1 
        
        while i < n:
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1 
            
        while j < m:
            if not res or res[-1] != b[j]:
                res.append(b[j])
            j += 1
            
        return res
                




#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends