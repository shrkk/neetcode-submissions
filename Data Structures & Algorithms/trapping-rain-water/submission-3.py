class Solution:
    def trap(self, height: List[int]) -> int:

        l, r  = 0, len(height) - 1
        area = 0
        leftMax, rightMax = height[l], height[r]

        while l < r:
            
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                area += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                area += rightMax - height[r]
        return area

