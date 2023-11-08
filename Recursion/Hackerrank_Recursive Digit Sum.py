#TLE
def superDigit(n: str, k: int):
    def fun(n: str):
        sm = 0
        for digit in n:
            sm += int(digit)
            
        sm = str(sm)
        if len(sm) == 1:
            return sm
        return fun(sm)
    
    return fun(n*k)

#===============================================================#
def superDigit(n: str, k: int):
    def fun(n: str):
        sm = 0
        for digit in n:
            sm += int(digit)
            
        sm = str(sm)
        if len(sm) == 1:
            return sm
        return fun(sm)
    
    p = fun(n)
    return fun(p*k)
