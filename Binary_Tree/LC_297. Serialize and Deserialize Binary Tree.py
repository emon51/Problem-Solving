
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return ''
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            res += [str(node.val)] if node else ['#']
            if not node:
                continue
            q.append(node.left)
            q.append(node.right)
        #print(res, ','.join(res))
        return ','.join(res)
            

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #return 
        if not data:
            return 
        data = data.split(',')
        root =  TreeNode(data[0])
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if i < len(data) and data[i] != '#':
                node.left = TreeNode(data[i])
                q.append(node.left)
            else:
                node.left = None
            i += 1
            if i < len(data) and data[i] != '#':
                node.right = TreeNode(data[i])
                q.append(node.right)
            else:
                node.right = None
            i += 1
        return root
            



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
