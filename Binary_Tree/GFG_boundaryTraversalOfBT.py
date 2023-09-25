#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        
        def _leaf(node):
            return not node.left and not node.right
        
        def left(node):
            cur = node 
            while cur and not _leaf(cur):
                left_nodes.append(cur.data)
                if cur.left:
                    cur = cur.left 
                else:
                    cur = cur.right 
        
        def right(node):
            cur = node 
            while cur and not _leaf(cur):
                right_nodes.append(cur.data)
                if cur.right:
                    cur = cur.right 
                else:
                    cur = cur.left 
        
        def leaf(node):
            if _leaf(node):
                leaf_nodes.append(node.data)
                return
            if node.left:
                leaf(node.left)
            if node.right:
                leaf(node.right)
        
        if _leaf(root):
            return [root.data]
            
        left_nodes = []
        right_nodes = []
        leaf_nodes = []
        
        left(root.left)
        right(root.right)
        leaf(root)
        
        return [root.data] + left_nodes + leaf_nodes + right_nodes[::-1]