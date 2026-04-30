class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r=len(board)
        c=len(board[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c and board[row][col]=='O'
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        seen=set()
        opening=False
        def dfs(row,col):
            nonlocal opening
            if (row==0) or (row==r-1) or (col==0) or (col==c-1):
                opening=True
                return
            if (row,col) in notSurrounded:
                opening=True
                return
            for dx,dy in direction:
                newRow=dx+row
                newCol=dy+col
                if ((newRow==0) or (newRow==r-1) or (newCol==0) or (newCol==c-1)) and valid(newRow,newCol):
                    opening=True
                    return
                elif (newRow,newCol) not in seen and valid(newRow,newCol):
                    seen.add((newRow,newCol))
                    dfs(newRow,newCol)            
        notSurrounded=set()
        for i in range(r):
            for j in range(c):
                if board[i][j]=='O':
                    opening=False
                    seen=set()
                    dfs(i,j)
                    if not opening:
                        board[i][j]='X'
                    else:
                        notSurrounded.add((i,j))
                        
                