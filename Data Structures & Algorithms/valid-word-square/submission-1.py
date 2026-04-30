class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        row={}
        col={}
        r=len(words)
        for i in range(r):
            c=len(words[i])
            j=0
            while j<c:
                if i not in row:
                    row[i]=[]
                if j not in col:
                    col[j]=[]
                row[i].append(words[i][j])
                col[j].append(words[i][j])
                j+=1
        return row==col