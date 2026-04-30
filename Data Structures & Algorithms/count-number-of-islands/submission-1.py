class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        cnt=0
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]=='1'
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        seen=set()
        def dfs(row,col):
            for dx,dy in directions:
                new_row=row+dx
                new_col=col+dy
                if valid(new_row,new_col) and (new_row,new_col) not in seen:
                    seen.add((new_row,new_col))
                    dfs(new_row,new_col)
        
        for i in range(r):
            for j in range(c):
                if (i,j) not in seen and grid[i][j]=='1':
                    seen.add((i,j))
                    dfs(i,j)
                    cnt+=1
        return cnt