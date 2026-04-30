class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        DP=[0]*(n+1)
        DP[1]=1
        DP[2]=2
        for i in range(3,len(DP)):
            DP[i]=DP[i-1]+DP[i-2]
        return DP[-1]