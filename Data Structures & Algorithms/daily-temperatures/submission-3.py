from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stack and curr > stack[-1][0]:
                snum, sidx = stack.pop()
                res[sidx] = i - sidx
            stack.append((curr, i))
        return res

        # [30,38,30,36,35,40,28]
        # stack -> [0], [40, ]

