class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        res = []
        self.groupHelper(strs, res)
        return res

    def groupHelper(self, strs: List[str], res: List[List[str]]) -> None:
        if not strs:
            return

        target = strs[0]
        current_group = [target]
        remaining = []

        for word in strs[1:]:
            if sorted(word) == sorted(target):
                current_group.append(word)
            else:
                remaining.append(word)

        res.append(current_group)
        self.groupHelper(remaining, res)
                    