class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def dfs(i):
            if i == n:
                res.append(["".join(row) for row in board])
                return
            
            for x in range(n):
                if x in col or (i - x) in posDiag or (i + x) in negDiag:
                    continue
                else:
                    col.add(x)
                    posDiag.add(i-x)
                    negDiag.add(i+x)
                    board[i][x] = "Q"
                    dfs(i + 1)
                    col.remove(x)
                    posDiag.remove(i-x)
                    negDiag.remove(i+x)
                    board[i][x] = "."
        dfs(0)
        return res
                

                
