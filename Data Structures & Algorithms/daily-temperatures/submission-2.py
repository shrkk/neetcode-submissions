from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        self.dailyTempHelper(temperatures, 0, res)
        return res

    def dailyTempHelper(self, temps: List[int], index: int, res: List[int]):
        if index >= len(temps):
            return

        i = index + 1
        while i < len(temps) and temps[i] <= temps[index]:
            i += 1

        if i < len(temps):
            res.append(i - index)
        else:
            res.append(0)

        self.dailyTempHelper(temps, index + 1, res)
