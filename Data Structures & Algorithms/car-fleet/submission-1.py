class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        stack2=[]
        for i in range(len(position)):
            stack2.append((position[i],speed[i]))
        stack2.sort()
        stack2.reverse()
        for car in stack2:
            pos,spd=car
            time=(target-pos)/spd
            if len(stack)==0:
                stack.append(time)
            else:
                if time<=stack[-1]:
                    pass
                else:
                    stack.append(time)
        return len(stack)