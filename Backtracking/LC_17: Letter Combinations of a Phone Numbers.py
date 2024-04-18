
'''
digits = '23'
output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if not digits:
            return []
            
        res = []
        def fun(s, i, n, p = ''):
            if i == n:
                res.append(p)
                return 
            for ch in mapp[s[i]]:
                fun(s, i + 1, n, p + ch)
        fun(digits, 0, len(digits))
        return res

        
