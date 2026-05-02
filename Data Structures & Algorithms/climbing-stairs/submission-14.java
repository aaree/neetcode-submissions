class Solution {
    public int climbStairs(int n) {
        if (n<2){
            return n;
        }
        int[] DP=new int[n];
        DP[0]=1;
        DP[1]=2;
        for(int i=2;i<DP.length;i++){
            DP[i]=DP[i-1]+DP[i-2];
        }
        return DP[DP.length-1];
    }
}
