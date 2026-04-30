class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal=99999999
        maxProfit=0
        for i in prices:
            minVal=min(minVal,i)
            Profit=i-minVal
            maxProfit=max(Profit,maxProfit)
        return maxProfit