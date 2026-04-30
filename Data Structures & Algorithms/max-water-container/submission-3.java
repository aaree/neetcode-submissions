class Solution {
    public int maxArea(int[] heights) {
        int l=0;
        int r = heights.length-1;
        int maxVal=0;
        while (r>l){
            int vol=(r-l)*Math.min(heights[r],heights[l]);
            maxVal=Math.max(vol,maxVal);
            if (heights[r]>=heights[l]){
                l++;
            }else{
                r--;
            }
        }
        return maxVal;
    }
}
