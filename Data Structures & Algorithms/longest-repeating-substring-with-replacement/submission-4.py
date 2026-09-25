class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        currMax = 0

        for right in range(len(s)):
            # while k is 0 and our current is not same char, shift till??
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1

            while (right - left + 1) - max(count.values()) > k:
                # remove the left character
                count[s[left]] -= 1
                left += 1
            currMax = max(currMax, right - left + 1)
        
        return currMax