class Solution {
    public int climbStairs(int n) {
        if (n<3){
            return n;
        }
        int[] DP=new int[n+1];
        DP[1]=1;
        DP[2]=2;
        for(int i=3;i<DP.length;i++){
            DP[i]=DP[i-1]+DP[i-2];
        }
        return DP[DP.length-1];

    }
}
