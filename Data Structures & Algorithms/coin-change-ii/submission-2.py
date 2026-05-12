class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        def dfs(pointer,total):
            if total==0:
                return 1
            elif total<0 or pointer>=len(coins):
                return 0
            if (pointer,total) in memo:
                return memo[(pointer,total)]
            t1=dfs(pointer+1,total)
            t2=dfs(pointer,total-coins[pointer])
            memo[(pointer,total)]=t1+t2
            return memo[(pointer,total)]
        return dfs(0,amount)