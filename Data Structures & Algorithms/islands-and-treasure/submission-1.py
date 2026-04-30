class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r=len(grid)
        c=len(grid[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]!=-1
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        queue=deque()
        step=1
        seen=set()        
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    queue.append((i,j))
        while len(queue)>0:
            for i in range(len(queue)):
                row,col=queue.popleft()
                for dx,dy in directions:
                    new_row=row+dx
                    new_col=col+dy
                    if valid(new_row,new_col) and grid[new_row][new_col]==2147483647 and (new_row,new_col) not in seen:
                        grid[new_row][new_col]=step
                        seen.add((new_row,new_col))
                        queue.append((new_row,new_col))
            step+=1