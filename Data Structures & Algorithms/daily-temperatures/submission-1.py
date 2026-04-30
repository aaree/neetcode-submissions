class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp=[]
        ans=[0]*len(temperatures)
        for i,val in enumerate(temperatures):
            if len(temp)==0:
                temp.append((i,val))
            else:
                while len(temp)>0 and val>temp[-1][1]:
                    one,two=temp.pop()
                    ans[one]=i-one
                    print(temp)
            temp.append((i,val))
        return ans