from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        curr = 0
        res = 0
        
        while curr < len(height) - 1:
            currheight = height[curr]
            next_bar = curr + 1
            max_in_rest = 0
            max_pos = -1
            
            # Find the next bar that is taller or equal (right boundary)
            while next_bar < len(height):
                if height[next_bar] >= currheight:
                    max_pos = next_bar
                    break
                if height[next_bar] >= max_in_rest:
                    max_in_rest = height[next_bar]
                    max_pos = next_bar
                next_bar += 1
            
            if max_pos == -1:
                break  # No right boundary
            
            # Find the min height between curr and the next highest bar
            bound_height = min(height[curr], height[max_pos])
            total = 0
            for i in range(curr + 1, max_pos):
                total += max(0, bound_height - height[i])
            
            res += total
            curr = max_pos
        
        return res
