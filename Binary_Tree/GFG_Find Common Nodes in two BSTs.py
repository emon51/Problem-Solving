from collections import deque 
class Solution:
    
    #Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        
        def fun(root):
            q = deque()
            q.append(root)
            res = []
            while q:
                p = q.popleft()
                res.append(p.data)
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            return res
            
        arr1, arr2 = set(fun(root1)), set(fun(root2))
        res = arr1.intersection(arr2)
        return sorted(list(res))
