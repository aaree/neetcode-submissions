class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue=deque()
        r=len(grid)
        c=len(grid[0])
        seen1=set()
        seen2=set()
        def valid(row,col):
            return 0<=row<r and 0<=col<c
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(row,col):
            for dx,dy in directions:
                new_row=row+dx
                new_col=col+dy
                if valid(new_row,new_col) and grid[new_row][new_col]==1 and (new_row,new_col) not in seen1:
                    seen1.add((new_row,new_col))
                    queue.append((new_row,new_col))
                    dfs(new_row,new_col)
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    seen1.add((i,j))
                    queue.append((i,j))
                    dfs(i,j)
                if len(queue)>0:
                    break
            if len(queue)>0:
                break                
        cnt=0
        while len(queue)>0:
            for i in range(len(queue)):
                row,col=queue.popleft()
                for dx,dy in directions:
                    new_row=row+dx
                    new_col=col+dy
                    if valid(new_row,new_col):
                        if cnt>0 and grid[new_row][new_col]==1 and (new_row,new_col) not in seen2 and (new_row,new_col) not in seen1:
                            print(new_row,new_col)
                            return cnt
                        elif grid[new_row][new_col]==0:
                            seen2.add((new_row,new_col))
                            print((new_row,new_col))
                            queue.append((new_row,new_col))
            cnt+=1
