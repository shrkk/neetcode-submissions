class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.findHelper(nums, 0, len(nums)-1)
    def findHelper(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]
        
        mid_index = (left + right) // 2
        mid_val = nums[mid_index]
        
        if mid_val < nums[right]:
            return self.findHelper(nums, left, mid_index)
        else:
            return self.findHelper(nums, mid_index + 1, right)
        