class Solution {
    public int maxProfit(int[] prices) {
        int maxVal=0;
        int minVal=9999999;
        int maxProfit=0;
        int profit;
        for (int price:prices){
            minVal=Math.min(minVal,price);
            profit=price-minVal;
            maxProfit=Math.max(maxProfit,profit);
        }
        return maxProfit;
    }
}
