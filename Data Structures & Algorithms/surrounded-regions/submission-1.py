class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r=len(board)
        c=len(board[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c and board[row][col]=='O'
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        seen=set()

        def dfs(row,col):
            nonlocal open
            if row==0 or row==r-1 or col==0 or col==c-1:
                open=True
                return
            for dx,dy in directions:
                newRow=row+dx
                newCol=col+dy
                if valid(newRow,newCol) and (newRow,newCol) not in seen:
                    seen.add((newRow,newCol))
                    dfs(newRow,newCol)
        for i in range(r):
            for j in range(c):
                if valid(i,j):
                    open=False
                    seen=set()
                    dfs(i,j)
                    if not open:
                        board[i][j]='X'
        

