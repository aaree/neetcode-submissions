class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        queue=deque()
        seen=set()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        time=0
        fresh=0
        def valid(row,col):
            nonlocal r
            nonlocal c
            nonlocal grid
            return 0<=row<r and 0<=col<c and grid[row][col]==1
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    queue.append((i,j))
                    seen.add((i,j))
                if grid[i][j]==1:
                    fresh+=1
        if len(queue)==0:
            if fresh==0:
                return 0
            else:
                return -1
        while len(queue)>0:
            if fresh==0:
                break
            for i in range(len(queue)):
                curr=queue.popleft()
                for d in directions:
                    dx,dy=d
                    row,col=curr
                    new_row=row+dx
                    new_col=col+dy
                    if valid(new_row,new_col):
                        queue.append((new_row,new_col))
                        grid[new_row][new_col]=2
                        fresh-=1
            time+=1
        if fresh==0:
            return time
        else:
            return -1
        
        