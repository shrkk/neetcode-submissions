class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        fruitFreshened = False
        
        def addFruit(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit
            or grid[r][c] == 0):
                return 
            fruitFreshened = True
            visit.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
        
        time = -1
        while q:
            for i in range(len(q)):
                r, c  = q.popleft()
                grid[r][c] = 2
                addFruit(r + 1, c)
                addFruit(r - 1, c)
                addFruit(r, c + 1)
                addFruit(r, c - 1)
            time += 1
        for x in grid:
            if 1 in x:
                return -1
        if time > 0:
            return time
        else:
            return 0