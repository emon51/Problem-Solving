class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        
        child_nodes = set(leftChild + rightChild)
        
        root = None
        for node in range(n):
            if node not in child_nodes:
                root = node
        if root == None:
            return False
        q = deque()
        q.append(root)
        vis = set()
        while q:
            p = q.popleft()
            if p in vis:
                return False
            vis.add(p)
            if leftChild[p] != -1:
                q.append(leftChild[p])
            if rightChild[p] != -1:
                q.append(rightChild[p])
        return len(vis) == n
            
