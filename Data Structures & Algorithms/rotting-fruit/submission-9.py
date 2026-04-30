class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]!=0
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        seen=set()
        queue=deque()
        time=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    seen.add((i,j))
                    queue.append((i,j))
        while queue:
            for i in range(len(queue)):
                row,col=queue.popleft()
                for dx,dy in directions:
                    newRow=row+dx
                    newCol=col+dy
                    if valid(newRow,newCol) and (newRow,newCol) not in seen:
                        grid[newRow][newCol]=2
                        seen.add((newRow,newCol))
                        queue.append((newRow,newCol))
            print(grid)
            if queue:
                time+=1
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    return -1
        return time