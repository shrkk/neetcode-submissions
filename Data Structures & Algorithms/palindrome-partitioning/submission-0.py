class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, curr):
            if i >= len(s):
                res.append(curr[:])   # found a valid partition
                return 
            j = i + 1
            while j <= len(s):
                substr = s[i:j]
                if substr == substr[::-1]:  # palindrome check
                    curr.append(substr)
                    dfs(j, curr)
                    curr.pop()              # backtrack
                j += 1

        dfs(0, [])
        return res
