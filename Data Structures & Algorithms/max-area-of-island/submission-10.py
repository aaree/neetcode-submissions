class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]==1
        seen=set()
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        island=1
        maxisland=0
        def dfs(row,col):
            nonlocal island
            for dx,dy in directions:
                newRow=row+dx
                newCol=col+dy
                if valid(newRow,newCol) and (newRow,newCol) not in seen:
                    seen.add((newRow,newCol))
                    island+=1
                    dfs(newRow,newCol)
        for i in range(r):
            for j in range(c):
                if (i,j) not in seen and valid(i,j):
                    island=1
                    seen.add((i,j))
                    dfs(i,j)
                    maxisland=max(maxisland,island)
        return maxisland