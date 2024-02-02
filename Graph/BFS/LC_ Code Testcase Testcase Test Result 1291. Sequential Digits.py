
from collections import deque

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        # Initialize the queue with single-digit numbers.
        q = deque(range(1, 10))
        res = []
        while q:
            num = q.popleft()

            if low <= num <= high:
                res.append(num)

            last_digit = num % 10

            if last_digit < 9:
                new_num = num * 10 + (last_digit + 1)
                if new_num <= high:
                    q.append(new_num)

        return res

