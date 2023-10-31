lass Solution:
    def countBits(self, n: int) -> List[int]:

        def _setbit(num):
            cnt = 0
            while num:
                cnt += (num & 1)
                num >>= 1
            return cnt

        res = []
        for num in range(n + 1):
            res.append(_setbit(num))
        return res

        
