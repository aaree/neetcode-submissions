class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        r=len(grid)
        c=len(grid[0])
        length=1
        def valid(row,col):
            nonlocal r
            nonlocal c
            nonlocal grid
            return 0<=row<r and 0<=col<c and grid[row][col]==0
        seen=set()
        queue=deque()
        queue.append((0,0))
        seen.add((0,0))
        directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        while len(queue)>0:
            for i in range(len(queue)):
                curr=queue.popleft()            
                for d in directions:
                    dx,dy=d
                    row,col=curr
                    new_row=row+dx
                    new_col=col+dy
                    if valid(new_row,new_col) and (new_row,new_col) not in seen:
                        print(new_row,new_col)
                        seen.add((new_row,new_col))
                        queue.append((new_row,new_col))
            length+=1
            if (r-1,c-1) in seen:
                break
        if (r-1,c-1) in seen:
            return length
        else:
            return -1