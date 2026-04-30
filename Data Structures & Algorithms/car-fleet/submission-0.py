class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack1=[]
        ans=[]
        for i in range(len(position)):
            stack1.append([position[i],speed[i]])
        stack1.sort(key=lambda x:-x[0])
        for position,speed in stack1:
            time=(target-position)/speed
            if len(ans)==0:
                ans.append(time)
            else:
                if time<=ans[-1]:
                    pass
                else:
                    ans.append(time)
        return len(ans)