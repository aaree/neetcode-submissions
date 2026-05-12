class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def DP(pointer,total):
            if total==0:
                return 0
            if total<0 or pointer>=len(coins):
                return math.inf
            if (pointer,total) in memo:
                return memo[(pointer,total)]
            total1=DP(pointer+1,total)
            total2=1+DP(pointer,total-coins[pointer])
            memo[(pointer,total)]=min(total1,total2)
            return memo[(pointer,total)]
        result=DP(0,amount)
        if result==math.inf:
            return -1
        else:
            return result