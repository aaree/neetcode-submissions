class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def dfs(pointer,cooldown,holding):
            if pointer==len(prices):
                return 0
            if (pointer,cooldown,holding) in memo:
                return memo[(pointer,cooldown,holding)]
            if cooldown:
                memo[(pointer,cooldown,holding)]= dfs(pointer+1,False,False)
            else:
                if holding:
                    memo[(pointer,cooldown,holding)]= max((prices[pointer]+dfs(pointer+1,True,False),dfs(pointer+1,False,True)))
                else:
                    memo[(pointer,cooldown,holding)]= max((-prices[pointer]+dfs(pointer+1,False,True),dfs(pointer+1,False,False)))
            return memo[(pointer,cooldown,holding)]
        return dfs(0,False,False)