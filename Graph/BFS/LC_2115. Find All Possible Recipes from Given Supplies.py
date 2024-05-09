
#Topological Sort
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        adj = defaultdict(lambda: [])
        indegree = defaultdict(int)

        for reci, ings in zip(recipes, ingredients):
            for ing in ings:
                adj[ing].append(reci)
                indegree[reci] += 1
        
        q =  deque(supplies)
        while q:
            u = q.popleft()
            for v in adj.get(u, []):
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        res = []
        for u, degree in indegree.items():
            if degree == 0:
                res.append(u)
        return res
