class Solution {

    public List<List<Integer>> twoSum(int target,int[] nums, int start){
        int l=start;
        int r=nums.length-1;
        List<List<Integer>> ans=new ArrayList<>();
        
        while (r>l){
            int total=nums[r]+nums[l];
            if (total>target){
                r--;
            }else if (total<target){
                l++;
            }else if (total==target){
                
                ans.add(Arrays.asList(-target,nums[l],nums[r]));
                while((r>l) && ((nums[l]==nums[l+1]))){
                    l++;
                }
                while((r>l) && ((nums[r]==nums[r-1]))){
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

        for(int i=0;i<nums.length;i++){
            if (nums[i]>0){
                break;
            }
            if ((i==0) || (nums[i]!=nums[i-1])){
                int target=nums[i];
                List<List<Integer>> next=twoSum(-target,nums,i+1);
                answer.addAll(next);
            }
        }
        return answer;
        
    }
}
