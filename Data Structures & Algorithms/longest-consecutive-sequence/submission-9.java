class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> seen=new HashSet<>();
        Set<Integer> set = new HashSet<>();
        int maxcnt=0;
        for (int num:nums){
            set.add(num);
        }
        for(int i=0;i<nums.length;i++){
            if (seen.contains(nums[i])){
                continue;
            }
            int cnt=0;
            int curr=nums[i];
            while (set.contains(curr)){
                cnt+=1;
                curr+=1;
                seen.add(curr);
                maxcnt=Math.max(maxcnt,cnt);                
            }
        }
        return maxcnt;


    }
}
