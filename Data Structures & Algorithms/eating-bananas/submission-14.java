class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l=1;
        int r=Arrays.stream(piles).max().orElse(0);
        while (r>l){
            int total=0;
            int m=(r+l)/2;
            for (int pile: piles){
                int hour=(int)Math.ceil((double)pile/m);
                total+=hour;
            }
            if(total>h){
                l=m+1;
            }
            else{
                r=m;
            }
        }
        return l;
    }
}
