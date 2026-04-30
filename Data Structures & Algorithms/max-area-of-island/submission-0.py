class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        def valid(r1,c1):
            nonlocal r
            nonlocal c
            nonlocal grid
            return 0<=r1<r and 0<=c1<c and grid[r1][c1]==1
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        max_size=0
        area=0
        seen=set()
        def dfs(row,col):
            nonlocal grid
            nonlocal max_size
            nonlocal area
            for d in directions:
                dx,dy=d
                new_row=row+dx
                new_col=col+dy
                if valid(new_row,new_col) and (new_row,new_col) not in seen:
                    area+=1
                    seen.add((new_row,new_col))
                    dfs(new_row,new_col)
        
        for i in range(r):
            for j in range(c):
                if valid(i,j) and (i,j) not in seen:
                    area+=1
                    seen.add((i,j))
                    dfs(i,j)
                    max_size=max(max_size,area)
                    area=0
        return max_size