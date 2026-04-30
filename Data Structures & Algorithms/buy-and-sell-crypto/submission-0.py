class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=right=0
        minval=float("inf")
        ans=0
        for i in range(len(prices)):
            curr=prices[i]
            minval=min(minval,curr)
            diff=curr-minval
            if diff>0:
                ans=max(ans,diff)
        return ans