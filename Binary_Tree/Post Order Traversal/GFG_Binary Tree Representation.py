
#Array to Binary Tree
'''
You are given an array nodes which represents the value of nodes of the binary tree in level order traversal. You are also given a root of the tree which has a value equal to nodes[0].

Your task to construct a binary tree by creating nodes for the remaining 6 nodes.

Example:

Input: 
nodes = [1 2 3 4 5 6 7]
Output: 
         1
       /   \
     2       3
   /  \     /  \
   4  5    6   7
Explanation: 
The 7 node binary tree is represented above.
'''

#User function Template for python3

class Solution:
    def createTree(self, root, nodes):
        if not root:
            return 
        
        def fun(i):
            if i >= len(nodes):
                return None 
            node = Node(nodes[i]) if i != 0 else root
            node.left = fun(2 * i + 1)
            node.right = fun(2 * i + 2)
            return node
        
        return fun(0)
