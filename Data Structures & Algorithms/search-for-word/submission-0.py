class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_exists=False
        seen=set()
        r=len(board)
        c=len(board[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(row,col,point,seen,wd):
            nonlocal word_exists
            if len(wd)==len(word):
                word_exists=True
                return
            if len(wd)>len(word):
                return
            for d in directions:
                dx,dy=d
                new_row=row+dx
                new_col=col+dy
                if valid(new_row,new_col) and (new_row,new_col) not in seen:
                    if board[new_row][new_col]==word[point+1]:
                        seen.add((new_row,new_col))
                        wd.append(board[new_row][new_col])
                        dfs(new_row,new_col,point+1,seen.copy(),wd.copy())
                        wd.pop()
                        seen.remove((new_row,new_col))
        for i in range(r):
            for j in range(c):
                if board[i][j]==word[0]:
                    s=set()
                    wor=[board[i][j]]
                    s.add((i,j))
                    dfs(i,j,0,s,wor)
        return word_exists
