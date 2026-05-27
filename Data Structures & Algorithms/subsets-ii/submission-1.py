class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def combinations(start, curr):
            if start >= len(nums):
                return
            for x in range(start, len(nums)):
                if x > start and nums[x] == nums[x - 1]:
                    continue
                curr.append(nums[x])
                res.append(curr.copy())
                combinations(x + 1, curr)
                curr.pop()

        combinations(0, [])
        res.append([])
        return res
