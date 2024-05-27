

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        
        def left(node):
            cur = node 
            while cur and (cur.left or cur.right):
                left_nodes.append(cur.data)
                cur = cur.left if cur.left else cur.right 
        
        def right(node):
            cur = node 
            while cur and (cur.left or cur.right):
                right_nodes.append(cur.data)
                cur = cur.right if cur.right else cur.left 
        
        def leaf(node):
            stack = []
            cur = node 
            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                node = stack.pop()
                if not node.left and not node.right:
                    leaf_nodes.append(node.data)
                cur = node.right
        
        if not root.left and not root.right:
            return [root.data]
            
        left_nodes = []
        right_nodes = []
        leaf_nodes = []
        
        left(root.left)
        right(root.right)
        leaf(root)
        
        return [root.data] + left_nodes + leaf_nodes + right_nodes[::-1]




#Problem from coding ninjas: https://www.naukri.com/code360/problems/boundary-traversal-of-binary-tree_790725?leftPanelTabValue=PROBLEM

# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# Functions to traverse on each part.
def traverseBoundary(root):

    if not root:
        return []
    if not root.left and not root.right:
        return [root.data]
    
    lefts = []
    bottom = []
    rights = []

    #Extract left side
    curr = root.left
    while curr and (curr.left or curr.right):
        lefts.append(curr.data)
        if curr.left:
            curr = curr.left 
        else:
             curr = curr.right 
    
    #Extract right side
    curr = root.right
    while curr and (curr.left or curr.right):
        rights.append(curr.data)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left 
    
    #Extract leaves using inorder traversal
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left 
        node = stack.pop()
        if not node.left and not node.right:
            bottom.append(node.data)
        curr = node.right
    
    
    return [root.data] + lefts + bottom + rights[:: - 1]
    

































        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
