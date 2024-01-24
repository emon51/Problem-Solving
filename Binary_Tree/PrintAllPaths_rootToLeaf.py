def dfs(root, p = []):
        if not root.left and not root.right:
          p += [root.val]
          res.append(p)
          return
        if root.left:
          dfs(root.left, p + [root.val]) 
        if root.right:
          dfs(root.right, p + [root.val])
      
      res = []
      dfs(root) 
      print(res)
