class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for x in range(len(board[0])):
            row = set()
            for y in range(len(board[0])):
                if board[x][y] == ".":
                    continue
                if board[x][y] in row:
                    return False
                
                row.add(board[x][y])
        #check cols
        for y in range(len(board[0])):
            col = set()
            for x in range(len(board[0])):
                if board[x][y] == ".":
                    continue
                else:
                    if board[x][y] in col:
                        return False
                    else:
                        col.add(board[x][y])
        #check grid
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True