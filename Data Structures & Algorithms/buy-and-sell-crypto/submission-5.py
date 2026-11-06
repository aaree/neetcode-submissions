class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        sell=0
        minVal=prices[0]
        while l<len(prices):
            minVal=min(minVal,prices[l])
            sell=max(sell,prices[l]-minVal)
            l+=1
        return sell