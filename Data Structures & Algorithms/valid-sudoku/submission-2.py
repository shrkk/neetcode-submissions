from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            dupes = {}
            for val in row:
                if val != ".":
                    if val in dupes:
                        return False
                    dupes[val] = 1

        # Check columns
        for col in range(9):
            dupes = {}
            for row in range(9):
                val = board[row][col]
                if val != ".":
                    if val in dupes:
                        return False
                    dupes[val] = 1

        # Check 3x3 squares
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                dupes = {}
                for i in range(3):
                    for j in range(3):
                        val = board[row_start + i][col_start + j]
                        if val != ".":
                            if val in dupes:
                                return False
                            dupes[val] = 1

        return True
