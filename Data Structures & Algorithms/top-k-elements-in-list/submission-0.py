class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for x in nums:
            if x not in res:
                res[x] = 1
            else:
                res[x] += 1
        fin = []
        while k > 0:
            pair = max(res.items(), key=lambda x: x[1])
            fin.append(pair[0])
            del res[pair[0]]
            k -= 1
        return fin