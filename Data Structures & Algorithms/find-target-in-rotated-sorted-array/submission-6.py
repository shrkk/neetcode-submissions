class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # find min element
        pivot = 0

        while l < r:
            mid = l + ((r - l) // 2)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        pivot = l

        def bsearch(l, r):
            while l <= r:
                mid = l + ((r - l) // 2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        result = bsearch(0, pivot - 1)
        if result != -1:
            return result

        return bsearch(pivot, len(nums) - 1)