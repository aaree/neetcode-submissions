class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        area=0
        r=len(grid)
        c=len(grid[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]==1
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        seen=set()
        def dfs(row,col):
            nonlocal area
            for dx,dy in directions:
                new_row=row+dx
                new_col=col+dy
                if (new_row,new_col) not in seen and valid(new_row,new_col):
                    area+=1
                    seen.add((new_row,new_col))
                    dfs(new_row,new_col)
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1 and (i,j) not in seen:
                    seen.add((i,j))
                    area+=1
                    dfs(i,j)
                    max_area=max(area,max_area)
                    area=0
        return max_area