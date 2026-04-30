class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        def dfs(pointer,total):
            if total==0:
                return 1
            if total<0 or pointer>=len(coins):
                return 0
            if (pointer,total) in memo:
                return memo[(pointer,total)]
            skip=dfs(pointer+1,total)
            keep=dfs(pointer,total-coins[pointer])
            memo[(pointer,total)]=skip+keep
            return memo[(pointer,total)]
        return dfs(0,amount)
