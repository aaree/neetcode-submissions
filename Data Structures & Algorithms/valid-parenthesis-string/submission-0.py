class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin=openMax=0
        for i in s:
            if i=='(':
                openMin+=1
                openMax+=1
            if i==')':
                openMin-=1
                openMax-=1
            if i=='*':
                openMin-=1
                openMax+=1
            if openMin<0:
                openMin=0
            if openMax<0:
                return False
        if openMin==0:
            return True
        else:
            return False