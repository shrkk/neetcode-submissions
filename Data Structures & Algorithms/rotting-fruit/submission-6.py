class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        seen = set()
        q = deque()
        time = -1

        def addFruits(r,c):
            if r >= rows or c >= cols or (r,c) in seen or grid[r][c] == 0 or r < 0 or c < 0:
                return
            seen.add((r,c))
            q.append([r,c])
        
        #1st pass, identify rotted fruits
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    seen.add((r,c))
                    q.append([r,c])
                    
        while q:
            for i in range(len(q)):
                
                r,c = q.popleft()
                grid[r][c] = 2
                addFruits(r-1,c)
                addFruits(r+1,c)
                addFruits(r,c-1)
                addFruits(r,c+1)
            #add time after each layer
            time += 1
        
        for x in grid:
            if 1 in x:
                return -1
        if time > 0:
            return time
        else:
            return 0
            
