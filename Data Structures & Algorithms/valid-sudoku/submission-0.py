class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={}
        columns={}
        box={}
        r=len(board)
        c=len(board[0])
        for i in range(r):
            for j in range(c):
                if i not in rows:
                    rows[i]=set()
                if j not in columns:
                    columns[j]=set()
                if (i//3,j//3) not in box:
                    box[(i//3,j//3)]=set()
                val=board[i][j]
                if val!='.':
                    if val in rows[i]:
                        return False
                    else:
                        rows[i].add(val)
                    if val in columns[j]:
                        return False
                    else:
                        columns[j].add(val)
                    if val in box[(i//3,j//3)]:
                        return False
                    else:
                        box[(i//3,j//3)].add(val)
        return True