class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        DP=[None]*n
        DP[0]=1
        DP[1]=2
        for i in range(2,len(DP)):
            DP[i]=DP[i-1]+DP[i-2]
        return DP[-1]