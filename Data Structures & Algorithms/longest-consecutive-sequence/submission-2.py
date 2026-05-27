class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))       # Remove duplicates

        if not nums:                 # Empty check BEFORE indexing
            return 0

        nums.sort()
        curr = [nums[0]]
        res = 0
        largest = 0

        for x in nums[1:]:
            if x == curr[-1]:
                continue
            elif x == curr[-1] + 1:
                res += 1
                if res > largest:
                    largest = res
            else:
                res = 0
            curr.append(x)

        return largest + 1