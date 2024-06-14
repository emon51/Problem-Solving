
#Leetcode: 250(Premimum)
'''
Problem statement
You are given a binary tree. Return the count of unival sub-trees in the given binary tree. In unival trees, all the nodes, below the root node, have the same value as the data of the root.

For example: for the binary tree, given in the following diagram, the number of unival trees is 5.


Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
0 <= N <= 10^5
0 <= data <= 10^4, where data is the value for a node.

Time Limit: 1sec
Sample Input 1:
1 1 1 -1 -1 -1 -1
Sample Output 1:
3
Sample Input 2:
1 2 3 2 -1 3 4 -1 -1 3 3 -1 -1 -1 -1 -1 -1
Sample Output 2:
6
Explanation to Sample Input 2:
The input binary tree will be represented as 

In the above diagram, the orange marked nodes are the root nodes of the unival sub-trees for the given binary tree.
'''

def countUnivalTrees(root):
    res = 0
    def dfs(root):
        nonlocal res
        if not root:
            return None 
        l = dfs(root.left)
        r = dfs(root.right)
        if (not l or l == root.data) and (not r or r == root.data):
            res += 1
            return root.data
        return float('inf')

    
    dfs(root)
    return res
