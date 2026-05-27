class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS = {}
        seenT = {}
        for char in s:
            if char not in seenS:
                seenS[char] = 1
            else:
                seenS[char] += 1
        for char in t:
            if char not in seenT:
                seenT[char] = 1
            else:
                seenT[char] += 1
        if seenT == seenS:
            return True
        else:
            return False