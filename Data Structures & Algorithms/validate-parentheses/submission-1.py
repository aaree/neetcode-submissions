class Solution:
    def isValid(self, s: str) -> bool:
        parDict={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if i not in parDict:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                elif stack[-1]==parDict[i]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False