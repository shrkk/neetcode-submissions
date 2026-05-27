class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxTotal = 0
        window = {}
        maxFreq = 0  # new

        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            maxFreq = max(maxFreq, window[s[r]])  # only updated when expanding window

            # total window size - most frequent char count > k → shrink
            if (r - l + 1) - maxFreq > k:
                window[s[l]] -= 1
                l += 1

            maxTotal = max(maxTotal, r - l + 1)
            r += 1

        return maxTotal
