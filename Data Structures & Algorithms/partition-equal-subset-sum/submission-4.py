class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        n=len(nums)+1
        target=sum(nums)//2
        DP=[[False]*(target+1) for i in range(n)]
        for i in range(n):
            DP[i][0]=True
        for i in range(1,n):
            for j in range(target+1):
                if j-nums[i-1]>=0:
                    DP[i][j]=DP[i-1][j] or DP[i-1][j-nums[i-1]]
        
        return DP[n-1][target]