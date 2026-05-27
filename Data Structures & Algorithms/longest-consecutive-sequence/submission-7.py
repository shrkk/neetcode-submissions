class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        ## add everything to set
        numSet = set(nums)
        maxLen = 0
        


        for num in numSet:
            if num - 1 not in numSet:
                currLen = 0
                while num + currLen in numSet:
                    currLen += 1
                if currLen > maxLen:
                    maxLen = currLen
                
            
        return maxLen 

            #rm min element, check if 1 greater than prev