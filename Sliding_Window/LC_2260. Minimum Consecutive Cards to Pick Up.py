class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float("inf"); l = 0; d = {}
        for r in range(len(cards)):
            d[cards[r]] = d.get(cards[r], 0) + 1
            while l <= r and cards[r] in d and d[cards[r]] > 1:
                res = min(res, r - l + 1)
                d[cards[l]] -= 1
                if d[cards[r]] == 0:
                    d.pop(cards[l])
                l += 1
        return res if res != float("inf") else -1
