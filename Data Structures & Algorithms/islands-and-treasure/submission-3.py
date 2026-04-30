class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r=len(grid)
        c=len(grid[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]!=-1
        seen=set()
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        queue=deque()
        steps=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    queue.append((i,j))
                    seen.add((i,j))
        while len(queue)>0:
            steps+=1
            for i in range(len(queue)):
                row,col=queue.popleft()
                for dx,dy in directions:
                    newRow,newCol=row+dx,col+dy
                    if valid(newRow,newCol) and (newRow,newCol) not in seen:
                        seen.add((newRow,newCol))
                        grid[newRow][newCol]=steps
                        queue.append((newRow,newCol))
                    

