class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def dfs(total,pointer):
            if total==0:
                return 0
            if pointer>=len(coins):
                return math.inf
            if (total,pointer) in memo:
                return memo[(total,pointer)]
            res1=dfs(total,pointer+1)
            if total-coins[pointer]>=0:
                res1=min(res1,1+dfs(total-coins[pointer],pointer))
            memo[(total,pointer)]=res1
            return memo[(total,pointer)]
        res=dfs(amount,0)
        if res==math.inf:
            return -1
        else:
            return res