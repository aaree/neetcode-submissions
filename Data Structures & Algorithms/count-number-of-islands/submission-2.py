class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen=set()
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        r=len(grid)
        c=len(grid[0])
        cnt=0
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]=='1'
        def dfs(row,col):
            for dx,dy in directions:
                new_row=row+dx
                new_col=col+dy
                if (new_row,new_col) not in seen and valid(new_row,new_col):
                    seen.add((new_row,new_col))
                    dfs(new_row,new_col)
        for i in range(r):
            for j in range(c):
                if (i,j) not in seen and grid[i][j]=='1':
                    seen.add((i,j))
                    cnt+=1
                    dfs(i,j)
        return cnt