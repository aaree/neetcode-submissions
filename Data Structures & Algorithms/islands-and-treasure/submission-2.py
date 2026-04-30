class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r=len(grid)
        c=len(grid[0])
        seen=set()
        queue=deque()
        cnt=1
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]!=-1
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    seen.add((i,j))
                    queue.append((i,j))
        while len(queue)>0:
            for i in range(len(queue)):
                row,col=queue.popleft()
                for dx,dy in directions:
                    new_row=dx+row
                    new_col=dy+col
                    if (new_row,new_col) not in seen and valid(new_row,new_col):
                        grid[new_row][new_col]=cnt
                        queue.append((new_row,new_col))
                        seen.add((new_row,new_col))
            cnt+=1