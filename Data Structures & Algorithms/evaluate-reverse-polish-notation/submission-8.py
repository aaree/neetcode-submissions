class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.isnumeric() or (i[0]=='-' and len(i)>1):
                isnum=True
            else:
                isnum=False
            if isnum==False:
                one=stack.pop()
                two=stack.pop()
                if i=='+':
                    total=int(one)+int(two)
                    stack.append(total)
                elif i=='-':
                    total=int(two)-int(one)
                    stack.append(total)
                elif i=='*':
                    total=int(two)*int(one)
                    stack.append(total)
                elif i=='/':
                    total=int(float(two)/float(one))
                    stack.append(total)
            elif isnum==True:
                stack.append(int(i))
        return stack[0]