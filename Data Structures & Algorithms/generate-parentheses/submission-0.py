class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        seen=set()
        def backtrack(s,open,close):
            if open==n and close==n and s not in seen:
                seen.add(s)
                ans.append(s)
                return
            if open<n:
                s+='('
                open+=1
                backtrack(s,open,close)
                s=s[:-1]
                open-=1
            if open>close:
                s+=')'
                close+=1
                backtrack(s,open,close)
        backtrack('',0,0)
        return ans