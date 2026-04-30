class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        seen=set()
        maxArea=0
        area=0
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]==1
        def dfs(row,col):
            nonlocal area
            for dx,dy in directions:
                newRow=row+dx
                newCol=col+dy
                if (newRow,newCol) not in seen and valid(newRow,newCol):
                    area+=1
                    seen.add((newRow,newCol))
                    dfs(newRow,newCol)
        
        for i in range(r):
            for j in range(c):
                if (i,j) not in seen and valid(i,j):
                    area=1
                    seen.add((i,j))
                    dfs(i,j)
                    maxArea=max(area,maxArea)
        
        return maxArea