class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        for x in range(len(nums)):
            diff = target - nums[x]
            if diff in sumMap:
                return [sumMap[diff], x]
            sumMap[nums[x]] = x 