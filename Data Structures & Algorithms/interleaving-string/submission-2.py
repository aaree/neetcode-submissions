class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)!=(len(s1)+len(s2)):
            return False
        memo={}
        def dfs(p1,p2,p3):
            nonlocal memo
            if p1==len(s1) and p2==len(s2) and p3==len(s3):
                return True
            if (p1<len(s1) and p2<len(s2)) and s1[p1]!=s3[p3] and s2[p2]!=s3[p3]:
                return False
            if (p1,p2) in memo:
                return memo[(p1,p2)]
            if (p1<len(s1) and p2<len(s2)) and s1[p1]==s3[p3] and s2[p2]==s3[p3]:
                memo[(p1,p2)]=(dfs(p1+1,p2,p3+1) or dfs(p1,p2+1,p3+1))
            elif p1<len(s1) and s1[p1]==s3[p3]:
                memo[(p1,p2)]= dfs(p1+1,p2,p3+1)
            elif p2<len(s2) and s2[p2]==s3[p3]:
                memo[(p1,p2)]= dfs(p1,p2+1,p3+1)
            else: 
                memo[(p1,p2)]=False
            return memo[(p1,p2)]
        return dfs(0,0,0)