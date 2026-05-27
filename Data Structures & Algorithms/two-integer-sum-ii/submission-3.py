class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers
        left = 0
        right = len(numbers) - 1
        # 2 cases:
        while left < right:
            # less, add
            sumNums = numbers[left] + numbers[right]
            if sumNums == target:
                return [left + 1, right + 1]
            elif sumNums < target:
                left += 1
            else:
                right -= 1
            # more, decrease