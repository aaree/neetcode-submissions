class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        maxArea=0
        seen=set()
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]==1
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r, c):
            if not valid(r, c) or (r, c) in seen:
                return 0

            seen.add((r,c))
            area = 1

            for dx, dy in directions:
                area += dfs(r+dx, c+dy)

            return area
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1 and (i,j) not in seen:
                    area=dfs(i,j)
                    maxArea=max(area,maxArea)
        return maxArea
