class Solution:
    def checkValidString(self, s: str) -> bool:
        lstack, sstack = [], []
        for i, v in enumerate(s):
            if v == "(":
                lstack.append(i)
            elif v == "*":
                sstack.append(i)
            else:
                if lstack:
                    lstack.pop()
                elif sstack:
                    sstack.pop()
                else:
                    return False
                
        while lstack and sstack and lstack[-1] < sstack[-1]:
            lstack.pop()
            sstack.pop()
            
        return lstack == []
            
