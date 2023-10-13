class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        p1, q1, p2, q2 = rec2
        
        if p2 <= x1 or  x2 <= p1 or y2 <= q1 or q2 <= y1:
            return False
        return True
        
