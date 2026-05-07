class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo={}
        def dfs(left,right):
            if right<left:
                return 0
            if right==left:
                return 1
            if (left,right) in memo:
                return memo[(left,right)]
            temp1=temp2=temp3=0
            if s[left]==s[right]:
                temp1=2+dfs(left+1,right-1)
            if s[left]!=s[right]:
                temp2=dfs(left+1,right)
                temp3=dfs(left,right-1)
            memo[(left,right)]= max(temp1,temp2,temp3)
            return memo[(left,right)]
        return dfs(0,len(s)-1)