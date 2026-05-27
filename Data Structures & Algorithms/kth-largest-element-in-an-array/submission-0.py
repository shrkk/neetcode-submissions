import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]       # negate to simulate max-heap
        heapq.heapify(nums)             # heapify in place
        res = None
        for _ in range(k):              # pop k times
            res = -heapq.heappop(nums)  # negate back
        return res
