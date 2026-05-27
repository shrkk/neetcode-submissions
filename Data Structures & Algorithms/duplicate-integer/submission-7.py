class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for int in nums:
            if int not in seen:
                seen.add(int)
            else:
                return True
        return False