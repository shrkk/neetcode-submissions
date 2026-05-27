class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for x in s:
            if x == "(" or x == "{" or x == "[":
                res.append(x)
            else:
                if len(res) == 0:
                    return False
                if x == ")" and res[-1] != "(":
                    return False
                elif x == "]" and res[-1] != "[":
                    return False
                elif x == "}" and res[-1] != "{":
                    return False
                res.pop()
        if len(res) != 0:
            return False
        else:
            return True
