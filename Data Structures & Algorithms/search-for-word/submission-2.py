class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        validString=False
        r=len(board)
        c=len(board[0])
        def valid(row,col):
            return 0<=row<r and 0<=col<c
        seen=set()
        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(row,col,string):
            nonlocal validString
            if string==word:
                validString=True
                return
            for dx, dy in directions:
                newRow=row+dx
                newCol=col+dy
                if valid(newRow,newCol) and (newRow,newCol) not in seen and board[newRow][newCol]==word[len(string)]:
                    seen.add((newRow,newCol))
                    string+=board[newRow][newCol]
                    dfs(newRow,newCol,string)
                    string=string[:-1]
                    seen.remove((newRow,newCol))
            
        for i in range(r):
            for j in range(c):
                seen=set()
                if board[i][j]==word[0]:
                    seen.add((i,j))
                    dfs(i,j,word[0])
        return validString