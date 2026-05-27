class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                curr.append(candidates[i])
                dfs(i + 1, curr, total + candidates[i])
                curr.pop()

        dfs(0, [], 0)
        return res
