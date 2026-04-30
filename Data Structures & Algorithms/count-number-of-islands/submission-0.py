class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        def valid(r1,c1):
            nonlocal r
            nonlocal c
            nonlocal grid
            return 0<=r1<r and 0<=c1<c and grid[r1][c1]=='1'
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        numisland=0
        seen=set()
        def dfs(row,col):
            nonlocal grid
            nonlocal seen
            for d in directions:
                dx,dy=d
                new_row=row+dx
                new_col=col+dy
                if valid(new_row,new_col) and (new_row,new_col) not in seen:
                    seen.add((new_row,new_col))
                    dfs(new_row,new_col)
                
        for i in range(r):
            for j in range(c):
                if valid(i,j) and (i,j) not in seen:
                    numisland+=1
                    seen.add((i,j))
                    dfs(i,j)
        return numisland