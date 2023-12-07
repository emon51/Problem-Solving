class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        
        hand.sort()
        n = len(hand)
        if n % k != 0:
            return False
        
        mapp = {}
        for num in hand:
            mapp[num] = mapp.get(num, 0) + 1
            
        for f in hand:
            if f in mapp:
                for nm in range(f, k + f):
                    if nm not in mapp:
                        return False
                    mapp[nm] -= 1
                    if mapp[nm] == 0:
                        del mapp[nm]
        return True
                
