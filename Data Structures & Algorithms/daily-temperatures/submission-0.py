class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        new_temp=[]
        for i in range(len(temperatures)):
            new_temp.append((i,temperatures[i]))
        stack=[]
        h={}
        for temp in new_temp:
            while stack and temp[1]>stack[-1][1]:
                h[stack.pop()]=temp
            stack.append(temp)
        ans=[]
        for i in new_temp:
            if i in h:
                ans.append(h[i][0]-i[0])
            else:
                ans.append(0)
        return ans
