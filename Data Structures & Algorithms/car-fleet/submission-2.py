class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        total=[]
        for i in range(len(position)):
            total.append((position[i],speed[i]))
        total.sort()

        for i in range(len(total)-1,-1,-1):
            car=total[i][0]
            spd=total[i][1]
            time=(target-car)/spd
            if len(stack)==0:
                stack.append(time)
            elif time>stack[-1]:
                stack.append(time)
        
        return len(stack)