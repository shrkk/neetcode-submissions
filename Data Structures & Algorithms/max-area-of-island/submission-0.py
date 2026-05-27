class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c, islands):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0):
                return 0
            islands += 1
            area = 1
            grid[r][c] = 0
            
            for dr, dc in directions:
                area += dfs(r + dr, c + dc, islands)
            return area
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    islands = max(islands, dfs(r,c,0))
        return islands