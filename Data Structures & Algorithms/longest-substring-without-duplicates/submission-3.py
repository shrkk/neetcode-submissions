class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        start = 0
        maxLen = 0

        for end in range(len(s)):
            while s[end] in sub:
                start += 1
                sub = s[start:end]
            sub += s[end]
            maxLen = max(maxLen, end - start + 1)
        
        return maxLen


