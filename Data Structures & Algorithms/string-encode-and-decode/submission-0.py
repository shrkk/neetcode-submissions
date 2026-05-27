class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for x in strs:
            res += (x + ";")
        return res
    def decode(self, s: str) -> List[str]:
        currstr = ""
        res = []
        for x in list(s):
            if x == ";":
                res.append(currstr)
                currstr = ""
            else:
                currstr += x
        return res
