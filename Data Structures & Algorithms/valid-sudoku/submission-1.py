class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row={}
        col={}
        box={}
        r=len(board)
        c=len(board[0])
        for i in range(r):
            for j in range(c):
                val=board[i][j]
                if val.isnumeric():
                    if i not in row:
                        row[i]=set()
                    if j not in col:
                        col[j]=set()
                    if (i//3,j//3) not in box:
                        box[(i//3,j//3)]=set()
                    if val in row[i]:
                        return False
                    if val in col[j]:
                        return False
                    if val in box[(i//3,j//3)]:
                        return False
                    row[i].add(val)
                    col[j].add(val)
                    box[(i//3,j//3)].add(val)
        return True