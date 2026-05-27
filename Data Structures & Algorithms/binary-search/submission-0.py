class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchHelper(nums, target, 0, len(nums) - 1)
        

        
    def searchHelper(self, nums: List[int], target: int, left: int, right: int) -> int:
        
        if left > right:
            return -1
        curr = left + (right - left) // 2

        if nums[curr] == target:
            return curr
        if nums[curr] > target:
            return self.searchHelper(nums, target, left, curr - 1)
        return self.searchHelper(nums, target, curr + 1, right)