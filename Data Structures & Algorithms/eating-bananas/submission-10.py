import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.minHelper(piles, h, 1, 1, max(piles), 10000)
    def minHelper(self, piles: List[int], h: int, k : int, left : int, right : int, currMin : int) -> int:
        k = (left + right) // 2
        
        currTotal = 0
        for x in piles:
            currTotal += math.ceil(x/k)
            if currTotal > h:
                return self.minHelper(piles, h, k, k+1, right, currMin)
        if left < k:
            return self.minHelper(piles, h, k, left, k, k)
        else:
            return k
