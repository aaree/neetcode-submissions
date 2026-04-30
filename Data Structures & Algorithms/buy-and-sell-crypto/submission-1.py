class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        minPrice=99999
        for i,val in enumerate(prices):
            minPrice=min(minPrice,val)
            profit=val-minPrice
            maxProfit=max(profit,maxProfit)
        return maxProfit