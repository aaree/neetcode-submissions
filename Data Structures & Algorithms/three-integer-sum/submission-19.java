class Solution {
    public List<List<Integer>> twoSum(int[] nums, int target, int start){
        int l=start;
        int r=nums.length-1;
        List<List<Integer>> ans=new ArrayList<>();
        while(r>l){
            int total=nums[l]+nums[r];
            if(total>target){
                r--;
            }
            else if(total<target){
                l++;
            }
            else if (total==target){
                List<Integer> temp=new ArrayList<>(Arrays.asList(-target,nums[l],nums[r]));
                ans.add(temp);
                while ((r>l)&&(nums[l]==nums[l+1])){
                    l++;

                }
                while ((r>l)&&(nums[r]==nums[r-1])){
                    r--;
                }
                l++;
                r--;
            }
        }
        return ans;

    }
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> answer=new ArrayList<>();
        for (int i=0;i<nums.length;i++){
            int target=nums[i];
            if (target>0){
                break;
            }
            if ((i==0) || ((i>0)&&(nums[i]!=nums[i-1]))){
                List<List<Integer>> temp=twoSum(nums,-target,i+1);
                answer.addAll(temp);
            }
        }
        return answer;
    }
}
