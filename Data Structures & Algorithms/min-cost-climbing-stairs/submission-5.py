class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<2:
            for i in range(2):
                return cost[i]
        DP=[0]*(len(cost)+1)
        DP[0]=cost[0]
        DP[1]=cost[1]
        for i in range(2,len(DP)-1):
            DP[i]=cost[i]+min(DP[i-1],DP[i-2])
        return min(DP[-2],DP[-3])

        