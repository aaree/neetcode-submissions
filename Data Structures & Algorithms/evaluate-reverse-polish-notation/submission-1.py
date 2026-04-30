class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.isnumeric():
                stack.append(i)
            elif i[0]=='-' and len(i)>1:
                stack.append(i)
            else:
                if i=='+':
                    val1=stack.pop()
                    val2=stack.pop()
                    val3=int(val1)+int(val2)
                    stack.append(str(val3))
                elif i=='*':
                    val1=stack.pop()
                    val2=stack.pop()
                    val3=int(val1)*int(val2)
                    stack.append(str(val3))
                elif i=='-':
                    val1=stack.pop()
                    val2=stack.pop()
                    val3=int(val2)-int(val1)
                    stack.append(str(val3))
                elif i=='/':
                    val1=stack.pop()
                    val2=stack.pop()
                    val3=int(int(val2)/int(val1))
                    stack.append(str(val3))
        return int(stack[-1])