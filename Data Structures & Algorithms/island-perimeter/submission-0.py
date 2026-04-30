class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        perimeter=0
        r=len(grid)
        c=len(grid[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]==1
        for i in range(r):
            for j in range(c):
                if grid[i][j]== 1:
                    val=4
                    for dx, dy in directions:
                        new_row=dx+i
                        new_col=dy+j
                        if valid(new_row,new_col):
                            val-=1
                    perimeter+=val
        return perimeter