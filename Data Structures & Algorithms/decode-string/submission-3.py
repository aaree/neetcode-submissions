class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            num,temp='',[]
            if i!=']':
                stack.append(i)
            else:
                while stack[-1]!='[':
                    temp.append(stack.pop())
                temp.reverse()
                temp=''.join(temp)
                stack.pop()
                
                while len(stack)>0 and stack[-1].isnumeric():
                    num+=stack.pop()
                num=num[::-1]
                print(temp)
                for i in range(int(num)):
                    stack.append(temp)
                print(stack)
        return ''.join(stack)