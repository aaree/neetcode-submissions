class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)

        for i, val in enumerate(temperatures):
            if len(stack)==0:
                stack.append((i,val))
            else:
                while stack and val>stack[-1][1]:
                    j,oldVal=stack.pop()
                    ans[j]=i-j
                stack.append((i,val))
        return ans