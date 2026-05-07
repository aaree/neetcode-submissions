class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo={}
        def dfs(i,a,b):
            if i==len(strs) or a>m or b>n:
                return 0
            if (i,a,b) in memo:
                return memo[(i,a,b)]
            res1=dfs(i+1,a,b)
            if a>=strs[i].count('0') and b>=strs[i].count('1'):
                res1=max(res1,1+dfs(i+1,a-strs[i].count('0'),b-strs[i].count('1')))
            memo[(i,a,b)]=res1
            return memo[(i,a,b)]
        return dfs(0,m,n)
            
            