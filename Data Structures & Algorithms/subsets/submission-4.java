class Solution {
    List<List<Integer>> answer;
    public void dfs(int [] nums, int pointer,List<Integer> arr){
        if (pointer==nums.length){
            List<Integer> clone=new ArrayList<>(arr);
            answer.add(clone);
            return;
        }
        dfs(nums,pointer+1,arr);
        if (pointer<nums.length){
            arr.add(nums[pointer]);
            dfs(nums,pointer+1,arr);
            arr.remove(arr.size()-1);
        }
        
    }
    public List<List<Integer>> subsets(int[] nums) {
        answer= new ArrayList<>();
        dfs(nums,0,new ArrayList<>());
        return answer;

    }
}
