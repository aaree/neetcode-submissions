class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row={}
        col={}
        lonely=0
        r=len(picture)
        c=len(picture[0])
        for i in range(r):
            for j in range(c):
                if picture[i][j]=='B':
                    row[i]=row.get(i,0)+1
                    col[j]=col.get(j,0)+1
        for i in range(r):
            for j in range(c):
                if picture[i][j]=='B':
                    if row[i]==1 and col[j]==1:
                        lonely+=1
        return lonely