class Solution:
    def calPoints(self, operations: List[str]) -> int:
        temp=[]
        for i in operations:
            if i.isnumeric():
                temp.append(int(i))
            if i.startswith('-'):
                temp.append(int(i))
            if i=='+':
                two=temp.pop()
                one=temp.pop()
                three=two+one
                temp.append(one)
                temp.append(two)
                temp.append(three)
            if i=='D':
                two=temp.pop()
                three=two*2
                temp.append(two)
                temp.append(three)
            if i=='C':
                temp.pop()
        ans=0
        for i in temp:
            ans+=i
        return ans