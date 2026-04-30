class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cnt=0
        r=len(grid)
        c=len(grid[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c and grid[row][col]==1
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        seen=set()
        queue=deque()
        ones=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    seen.add((i,j))
                    queue.append((i,j))
                elif grid[i][j]==1:
                    ones+=1
        if len(queue)==0:
            if ones>0:
                return -1
            else:
                return 0
        while len(queue)>0:
            for i in range(len(queue)):
                row,col=queue.popleft()
                for dx,dy in directions:
                    new_row=row+dx
                    new_col=col+dy
                    if (new_row,new_col) not in seen and valid(new_row,new_col):
                        grid[new_row][new_col]=2
                        seen.add((new_row,new_col))
                        queue.append((new_row,new_col))
            cnt+=1
        ones=0
        print(grid)
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    return -1
        return cnt-1