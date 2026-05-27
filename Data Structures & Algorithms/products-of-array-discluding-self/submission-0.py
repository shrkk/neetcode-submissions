class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 0 
        res = []
        while x < len(nums):
            left = 1
            right = 1
            for y in nums[0:x]:
                left *= y
            for z in nums[x+1:]:
                right *= z
            res.append(left*right)
            x += 1
        return res
