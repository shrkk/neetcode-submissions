class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minVal = self.findHelper(nums, 0, len(nums)-1)
        sortedNums = []
        half1 = self.findTarget(nums[minVal:], 0, len(nums[minVal:])-1, target)
        half2 = self.findTarget(nums[:minVal], 0, len(nums[:minVal])-1, target)
        if half1 != -1:
            return half1 + minVal
        elif half2 != -1:
            return half2
        else:
            return -1

    def findHelper(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return left
        
        mid_index = (left + right) // 2
        mid_val = nums[mid_index]
        
        if mid_val < nums[right]:
            return self.findHelper(nums, left, mid_index)
        else:
            return self.findHelper(nums, mid_index + 1, right)
    def findTarget(self, nums: List[int], left: int, right: int, target) -> int:
        if left > right:
            return -1
        
        mid_index = (left + right) // 2
        mid_val = nums[mid_index]

        if mid_val == target:
            return mid_index
        elif mid_val > target:
            return self.findTarget(nums, left, mid_index - 1, target)
        else:
            return self.findTarget(nums, mid_index + 1, right, target)
