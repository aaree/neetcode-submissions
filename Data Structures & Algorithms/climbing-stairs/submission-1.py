class Solution:
    def climbStairs(self, n: int) -> int:
        memo=[0]*(n+1)
        if n==0:
            return 1
        if n<0:
            return 0
        if memo[n]!=0:
            return memo[n]
        else:
            memo[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
            return memo[n]
        
