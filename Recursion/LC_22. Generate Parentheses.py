class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def fun(l, r, p = ""):
            if l == 0 and r == 0:
                res.append(p)
                return 
            if l >= 0:
                fun(l - 1, r, p + "(")
            if l < r:
                fun(l, r - 1, p + ")")
            
        res = []
        fun(n, n)
        return res
        
