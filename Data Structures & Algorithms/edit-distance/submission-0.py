class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo={}
        def dfs(p1,p2):
            nonlocal memo
            if p1==len(word1):
                return len(word2)-p2
            if p2==len(word2):
                return len(word1)-p1
            if (p1,p2) in memo:
                return memo[(p1,p2)]
            if word1[p1]==word2[p2]:
                memo[(p1,p2)]=dfs(p1+1,p2+1)
            else:
                replace=1+dfs(p1+1,p2+1)
                delete=1+dfs(p1+1,p2)
                insert=1+dfs(p1,p2+1)
                memo[(p1,p2)]=min(replace,insert,delete)
            return memo[(p1,p2)]
        return dfs(0,0)
