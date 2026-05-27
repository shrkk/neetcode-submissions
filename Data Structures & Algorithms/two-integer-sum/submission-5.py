class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        index = 0
        for x in nums:
            if (target - x) in vals:
                return [vals[target-x], index]
            else:
                vals[x] = index
            index += 1
