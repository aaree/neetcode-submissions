class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for t in tokens:
            if t.isnumeric() or (t.startswith('-') and len(t)>1):
                stack.append(t)
            elif t=='+':
                one=stack.pop()
                two=stack.pop()
                stack.append(str(int(one)+int(two)))
            elif t=='*':
                one=stack.pop()
                two=stack.pop()
                stack.append(str(int(one)*int(two)))
            elif t=='-':
                one=stack.pop()
                two=stack.pop()
                stack.append(str(int(two)-int(one)))
            elif t=='/':
                one=stack.pop()
                two=stack.pop()
                stack.append(str(int(int(two)/int(one))))
        return int(stack[-1])
