class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i,val in enumerate(temperatures):
            if len(stack)==0:
                stack.append((i,val))
            else:
                while len(stack)>0 and val>stack[-1][1]:
                    pos,temp=stack.pop()
                    ans[pos]=i-pos
                stack.append((i,val))
        return ans