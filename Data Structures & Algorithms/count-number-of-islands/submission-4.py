class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        seen=set()
        numIslands=0
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]=='1'
        def dfs(row,col):
            for dx, dy in directions:
                newRow=row+dx
                newCol=col+dy
                if (newRow,newCol) not in seen and valid(newRow,newCol):
                    seen.add((newRow,newCol))
                    dfs(newRow,newCol)
        
        for i in range(r):
            for j in range(c):
                if (i,j) not in seen and valid(i,j):
                    seen.add((i,j))
                    numIslands+=1
                    dfs(i,j)
        return numIslands