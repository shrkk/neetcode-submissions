class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        
        # Use a for loop to safely pick the fixed element
        for x in range(len(nums)):
            # 1. Skip duplicate 'x' values to avoid redundant work
            if x > 0 and nums[x] == nums[x - 1]:
                continue
                
            left = x + 1
            right = len(nums) - 1
            
            while left < right:
                currSum = nums[left] + nums[x] + nums[right]
                
                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                else:
                    # 2. When match is found, add to res
                    res.append([nums[x], nums[left], nums[right]])
                    
                    # 3. CRITICAL: Advance pointers to avoid infinite loop
                    left += 1
                    right -= 1
                    
                    # 4. Skip duplicate pointers for 'left' and 'right'
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return res