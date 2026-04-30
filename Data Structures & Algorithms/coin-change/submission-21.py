class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def dfs(total,pointer):
            nonlocal memo
            if total==amount:
                return 0
            if total>amount or pointer>=len(coins):
                return math.inf
            if (total,pointer) in memo:
                return memo[(total,pointer)]
            skip=dfs(total,pointer+1)
            include=1+dfs(total+coins[pointer],pointer)
            memo[(total,pointer)]=min(skip,include)
            return memo[(total,pointer)]
        
        ans=dfs(0,0)
        if ans==math.inf:
            return -1
        else:
            return ans
            