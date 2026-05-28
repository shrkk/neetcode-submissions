class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        totalMax = 0

        while left < right:
            currMax = min(heights[left], heights[right]) * (right - left)
            totalMax = max(currMax, totalMax)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return totalMax