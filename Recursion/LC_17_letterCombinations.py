#Leetcode: 17 

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
      d = {
     "1":"",
     "2":"abc",
     "3":"def",
     "4":"ghi",
     "5":"jkl",
     "6":"mno",
     "7":"pqrs",
     "8":"tuv",
     "9":"wxyz"
   };
      
      res = []
      if digits == "":
        return res
      
      #p: process, up: unprocess
      def foo(i, p = ""):
        if i == len(digits):
          res.append(p)
          return 
        for ch in d[digits[i]]:
          foo(i + 1, p + ch)
        
      foo(0)
      return res
            
          
        