class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        for x in range(len(s)):
            if x == len(s)//2:
                return True
            if s[x] != s[len(s)-x-1]:
                return False
        return True