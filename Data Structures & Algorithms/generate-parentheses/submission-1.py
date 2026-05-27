from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.genParenHelper("", n, n, result)
        return result
    
    def genParenHelper(self, currStr: str, openNum: int, closedNum: int, result: List[str]):
        if openNum == 0 and closedNum == 0:
            result.append(currStr)
            return
        
        if openNum > 0:
            self.genParenHelper(currStr + "(", openNum - 1, closedNum, result)
        
        if closedNum > openNum:
            self.genParenHelper(currStr + ")", openNum, closedNum - 1, result)
