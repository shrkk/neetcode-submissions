class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []
        result = [0] * len(nums)

        curr = 1
        for num in nums:
            curr = num * curr 
            pre.append(curr)
        curr = 1
        for num in nums[::-1]:
            curr = num * curr 
            suf.append(curr)
        suf = suf[::-1]
        print(pre)
        print(suf)

        # prefixes and suffixes populated

        # edge case handling
        # element 0 should be suf[1]
        # element n-1 should be pre[-2]
        result[0] = suf[1]
        result[-1] = pre[-2]
        for x in range(1, len(nums)-1):
            
            prenum = pre[x-1]
            sufnum = suf[x+1]
            result[x] = (prenum * sufnum)
        return result