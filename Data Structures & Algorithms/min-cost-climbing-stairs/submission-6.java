class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] DP=new int[cost.length+1];
        DP[0]=0;
        DP[1]=0;
        for(int i=2;i<DP.length;i++){
            DP[i]=Math.min(cost[i-1]+DP[i-1],cost[i-2]+DP[i-2]);
        }
        return DP[DP.length-1];
    }
}
