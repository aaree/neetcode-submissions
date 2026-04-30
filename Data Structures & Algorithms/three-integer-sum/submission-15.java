class Solution {
    public Set<List<Integer>> twoSum(int target, int[] nums,int start){
        int l=start;
        int r=nums.length-1;
        Set<List<Integer>> set=new HashSet<>();
        while (r>l){
            int total=nums[r]+nums[l];
            if(total<target){
                l++;
            }else if(total>target){
                r--;
            }else if(total==target){
                List<Integer> list=new ArrayList<>(List.of(-target,nums[l],nums[r]));
                set.add(list);
                r--;
                l++;
            }
        }
        return set;
    }
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> answer=new HashSet<>();
        //List<List<Integer>>ans=new ArrayList<>();
        for (int i=0;i<nums.length;i++){
            if (nums[i]>0){
                break;
            }
            if ((i==0)||(i>0)&&(nums[i]!=nums[i-1])){
                int target=nums[i];
                Set<List<Integer>> newset=twoSum(-target,nums,i+1);
                answer.addAll(newset);
            }
        }
        List<List<Integer>> ans = new ArrayList<>(answer);
        ans.sort(Comparator.<List<Integer>>comparingInt(a -> a.get(0))
            .thenComparingInt(a -> a.get(1))
            .thenComparingInt(a -> a.get(2)));
        return ans;
    }
    
}
