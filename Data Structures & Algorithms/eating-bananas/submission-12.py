class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minhrs = r

        while l <= r:
            mid = l + ((r - l) // 2)
            hrs = 0

            for count in range(len(piles)):
                hrs += math.ceil(float(piles[count]) / mid)
            
            if hrs <= h:
                
                minhrs = min(minhrs, mid)

                r = mid - 1
            else:
                l = mid + 1
        
        return minhrs
            


            
