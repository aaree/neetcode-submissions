class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<2:
            return 0
        DP=[None]*(len(cost)+1)
        DP[0]=0
        DP[1]=0
        print(DP)
        for i in range(2,len(DP)):
            DP[i]=min(DP[i-1]+cost[i-1],DP[i-2]+cost[i-2])
        return DP[-1]

        