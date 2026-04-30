class Solution:
    def isValid(self, s: str) -> bool:
        complete={']':'[',')':'(','}':'{'}
        ans=[]
        for i in s:
            if i in complete:
                if len(ans)>0:
                    if complete[i]==ans[-1]:
                        ans.pop()
                    else:
                        return False
                else:
                    return False
            else:
                ans.append(i)
        
        return len(ans)==0