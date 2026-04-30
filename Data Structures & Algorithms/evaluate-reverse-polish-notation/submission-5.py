class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.isnumeric():
                stack.append(i)
            elif i.startswith('-') and len(i)>1:
                stack.append(i)
            elif i=='+':
                one=int(stack.pop())
                two=int(stack.pop())
                final=one+two
                stack.append(final)
            elif i=='-':
                one=int(stack.pop())
                two=int(stack.pop())
                final=two-one
                stack.append(final)
            elif i=='*':
                one=int(stack.pop())
                two=int(stack.pop())
                final=one*two
                stack.append(final)
            elif i=='/':
                one=int(stack.pop())
                two=int(stack.pop())
                final=int(two/one)
                stack.append(final)
        return int(stack[-1])