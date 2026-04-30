class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l=0;
        int r=0;
        int total=0;
        int minWindow=Integer.MAX_VALUE;
        while (r<nums.length){
            total+=nums[r];
            while (total>=target){
                if (total>=target){
                    int window=r-l+1;
                    minWindow=Math.min(minWindow,window);
                }
                total-=nums[l];
                l++;
                
            }
            r++;
        }
        if (minWindow<Integer.MAX_VALUE){
            return minWindow;        
        }
        return 0;
    }
}