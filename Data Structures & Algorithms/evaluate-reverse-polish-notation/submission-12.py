class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ans=0
        for i in tokens:
            print(stack)
            if i.isnumeric():
                stack.append(int(i))
            elif len(i)>1:
                stack.append(int(i))
            elif i=='+':
                one=stack.pop()
                two=stack.pop()
                stack.append(one+two)
            elif i=='-':
                one=stack.pop()
                two=stack.pop()
                stack.append(two-one)
            elif i=='*':
                one=stack.pop()
                two=stack.pop()
                stack.append(one*two)
            elif i=='/':
                one=stack.pop()
                two=stack.pop()
                stack.append(int(two/one))
        return stack[-1]