class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers)-1
        x = 0
        while x < len(numbers):
            currsum = numbers[x] + numbers[right]
            if (currsum > target):
                right -= 1
            elif (currsum < target):
                x += 1
            else:
                return [x + 1, right + 1]
            