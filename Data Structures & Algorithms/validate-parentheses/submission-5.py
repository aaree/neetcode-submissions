class Solution:
    def isValid(self, s: str) -> bool:
        bracket={']':'[','}':'{',')':'('}
        temp=[]
        for i in s:
            if len(temp)>0 and i in bracket:
                if bracket[i]==temp[-1]:
                    temp.pop()
                else:
                    temp.append(i)
            else:
                temp.append(i)
        if len(temp)==0:
            return True
        else:
            return False
                