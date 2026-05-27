class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(curr, i):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for x in digitToChar[digits[i]]:
                dfs(curr + x, i + 1)
        if digits:
            dfs("", 0)
        return res



            