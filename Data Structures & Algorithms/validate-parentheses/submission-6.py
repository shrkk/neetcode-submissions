from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for char in s:
            if char in ")}]":
                if len(q) == 0:
                    return False
                inner = q.pop()
                if char == ")" and inner != "(":
                    return False
                if char == "}" and inner != "{":
                    return False
                if char == "]" and inner != "[":
                    return False
            else:
                q.append(char)
        if len(q) == 0:
            return True
        else:
            return False