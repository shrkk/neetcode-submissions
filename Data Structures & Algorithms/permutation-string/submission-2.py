class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s1map = {}
        for x in s1:
            if x not in s1map:
                s1map[x] = 1
            else:
                s1map[x] += 1

        s2 = list(s2)
        count = 0
        s1_len = len(s1)
        for i in range(len(s2)):
            s1mapE = s1map.copy()
            count = 0
            for j in range(i, len(s2)):
                if s2[j] not in s1mapE:
                    break
                s1mapE[s2[j]] -= 1
                if s1mapE[s2[j]] == 0:
                    del s1mapE[s2[j]]
                count += 1
                if count == s1_len:
                    return True
        return False
