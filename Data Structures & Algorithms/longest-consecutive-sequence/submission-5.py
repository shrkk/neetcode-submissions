class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        ## add everything to set
        numSet = set()
        maxLen = 0
        currLen = 0

        for num in nums:
            numSet.add(num)
        #while loop while set not empty
        prev = min(numSet) - 1

        while len(numSet) != 0:
            curr = min(numSet)
            numSet.remove(curr)

            #debugging
            print(prev)
            print(curr)

            if curr != prev + 1:
                currLen = 0
            prev = curr
            if currLen > maxLen:
                maxLen = currLen
            currLen += 1
            
        return maxLen + 1

            #rm min element, check if 1 greater than prev