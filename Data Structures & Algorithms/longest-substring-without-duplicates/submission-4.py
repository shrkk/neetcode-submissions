class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        start = 0
        maxLen = 0

        for end in range(len(s)):
            while s[end] in sub:
                sub.remove(s[start])
                start += 1
            sub.add(s[end]) 
            maxLen = max(maxLen, end - start + 1)
        
        return maxLen


