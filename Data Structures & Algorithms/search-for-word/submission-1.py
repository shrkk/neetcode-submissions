class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = []
        hashPath = {}

        def dfs(x, y, i):
            # base case: found whole word
            if i == len(word):
                return True

            # out of bounds or already used or mismatch
            if (x < 0 or y < 0 or 
                x >= rows or y >= cols or 
                (x, y) in hashPath or 
                board[x][y] != word[i]):
                return False

            # choose
            hashPath[(x, y)] = 1
            path.append((x, y))

            # explore neighbors (down, up, right, left)
            res = (dfs(x + 1, y, i + 1) or
                   dfs(x - 1, y, i + 1) or
                   dfs(x, y + 1, i + 1) or
                   dfs(x, y - 1, i + 1))

            # unchoose (backtrack)
            path.pop()
            del hashPath[(x, y)]

            return res

        # try every starting cell
        for x in range(rows):
            for y in range(cols):
                if dfs(x, y, 0):
                    return True
        return False
