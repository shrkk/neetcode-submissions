class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for k in range(len(nums)+1)]
        resmap = {}
        for num in nums:
            if num not in resmap:
                resmap[num] = 1
            else:
                resmap[num] += 1
        for num, count in resmap.items():
            if buckets[count] != 0:
                buckets[count].append(num)
            else:
                buckets[count] = [num]
        result = []
        for numset in buckets[::-1]:
            for num in numset:
                if len(result) == k:
                    return result
                if num != None:
                    result.append(num)
        return result