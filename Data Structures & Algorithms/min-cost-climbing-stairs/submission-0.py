class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans=[0 for i in range(len(cost)+1)]
        ans[0]=0
        ans[1]=0
        for i in range(2,len(ans)):
            ans[i]=min(ans[i-2]+cost[i-2],ans[i-1]+cost[i-1])
        return ans[-1]