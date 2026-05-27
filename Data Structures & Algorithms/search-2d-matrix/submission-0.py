class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in range(len(matrix)):
            curr = self.searchHelper(matrix[x], target, 0, len(matrix[x]) - 1)
            if curr != -1:
                return True
        return False

        
    def searchHelper(self, nums: List[int], target: int, left: int, right: int) -> int:
        
        if left > right:
            return -1
        if right - left == 1:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1

        curr = left + (right - left) // 2


        if nums[curr] == target:
            return curr
        if nums[curr] > target:
            return self.searchHelper(nums, target, left, curr - 1)
        return self.searchHelper(nums, target, curr + 1, right)