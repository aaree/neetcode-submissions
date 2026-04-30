class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        open=0
        for i in s:
            if i.isalpha():
                stack.append(i)
            if i=='(':
                open+=1
                stack.append(i)
            if i==')':
                if open==0:
                    continue
                else:
                    open-=1
                    stack.append(i)
        print(open)
        if open==0:
            return ''.join(stack)
        else:
            final=[]
            for i in range(len(stack)-1,-1,-1):
                if stack[i].isalpha():
                    final.append(stack[i])
                if stack[i] == ')':
                    final.append(stack[i])
                if stack[i]=='(':
                    if open>0:
                        open-=1
                    else:
                        final.append(stack[i])
            final.reverse()
            return ''.join(final)
