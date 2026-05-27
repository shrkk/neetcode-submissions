class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        minWindows = []  # will store (length, substring)

        scount = 0
        tmap = {}
        windowMap = {}

        # Build target map
        for x in t:
            if x not in tmap:
                tmap[x] = 1
            else:
                tmap[x] += 1

        tcount = len(tmap)  # number of unique chars needed

        for r in range(len(s)):
            if s[r] in tmap:
                if s[r] not in windowMap:
                    windowMap[s[r]] = 1
                else:
                    windowMap[s[r]] += 1

                if windowMap[s[r]] == tmap[s[r]]:
                    scount += 1

            # shrink window when all chars satisfied
            while scount == tcount:
                minWindows.append((r - l + 1, s[l:r+1]))

                if s[l] in tmap:
                    windowMap[s[l]] -= 1
                    if windowMap[s[l]] < tmap[s[l]]:
                        scount -= 1
                l += 1

        return min(minWindows, default=(0, ""))[1]
