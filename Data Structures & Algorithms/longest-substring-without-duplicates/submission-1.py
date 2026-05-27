class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        s = list(s)
        dupe = []
        curr = 0
        maxTotal = 0

        for x in s:
            if x not in dupe:
                dupe.append(x)
                curr += 1
            else:
                while dupe[0] != x:
                    dupe.pop(0)
                dupe.pop(0)  # Remove the duplicate itself
                dupe.append(x)
                curr = len(dupe)

            maxTotal = max(maxTotal, curr)

        return maxTotal
