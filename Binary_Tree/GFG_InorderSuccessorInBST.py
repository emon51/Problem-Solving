

#TLE
'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        #store inorder traversal and immediate greater value than x.data will be required output.
        
        def inorder(root):
            if root.left:
                inorder(root.left)
            arr.append(root)
            if root.right:
                inorder(root.right)
                
        arr = [] #nodes
        inorder(root)
        
        for node in arr:
            if x.data < node.data:
                return node
                

#Optimal 
#User function Template for python3

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        
        cur = root 
        successor = None
        while cur:
            if x.data < cur.data:
                successor = cur
                cur = cur.left
            else:
                cur = cur.right
        return successor 
                
                