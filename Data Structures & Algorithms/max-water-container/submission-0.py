class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        res = []
        while left < right:
            leftv  = heights[left]
            rightv = heights[right]
            
            if leftv < rightv:
                res.append(leftv * len(heights[left:right]))
                left += 1
            else:
                res.append(rightv * len(heights[left:right]))
                right -= 1
        return max(res)
            
            
            