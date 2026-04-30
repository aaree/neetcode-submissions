class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l=1;
        int r=0;
        for (int n:piles){
            r=Math.max(r,n);
        }
        while (r>l){
            int m=(r+l)/2;
            int hour=0;
            for (int num : piles){
                hour+=Math.ceil((double)num/m);
            }
            if (hour>h){
                l=m+1;
            }else{
                r=m;
            }
        }
        return l;
    }
}
