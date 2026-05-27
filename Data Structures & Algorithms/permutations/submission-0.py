import math

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def combinations(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
            for x in range(len(nums)):
                if nums[x] in curr:
                    continue
                curr.append(nums[x])
                combinations(curr)
                curr.pop()

        combinations([])
        return res


