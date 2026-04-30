class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction=[(0,1),(1,0),(-1,0),(0,-1),(-1,1),(-1,-1),(1,-1),(1,1)]
        r=len(grid)
        c=len(grid[0])
        if grid[0][0]==1 or grid[r-1][c-1]==1:
            return -1
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]==0
        queue=deque()
        queue.append((0,0))
        seen=set()
        cnt=1
        final=-1
        finished=False
        while len(queue)>0:
            if finished==True:
                break
            for i in range(len(queue)):
                row,col=queue.popleft()
                for dx,dy in direction:
                    new_row=row+dx
                    new_col=col+dy
                    if valid(new_row,new_col) and (new_row,new_col) not in seen:
                        if (new_row,new_col)==(r-1,c-1):
                            return cnt+1
                        else:
                            seen.add((new_row,new_col))
                            queue.append((new_row,new_col))
            cnt+=1
        return final