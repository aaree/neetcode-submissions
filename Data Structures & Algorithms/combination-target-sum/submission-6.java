class Solution {
    List<List<Integer>> answer;
    public void dfs(int[] nums,int target,List<Integer> arr,int pointer){
        if (arr.stream().mapToInt(Integer::intValue).sum()==target){
            List<Integer> clone=new ArrayList<>(arr);
            answer.add(clone);
            return;
        }
        if ((pointer>=nums.length)||(arr.stream().mapToInt(Integer::intValue).sum()>target)){
            return;
        }
        if (pointer<nums.length){
            arr.add(nums[pointer]);
            dfs(nums,target,arr,pointer);
            arr.remove(arr.size()-1);
        }
        dfs(nums,target,arr,pointer+1);


    }
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        answer=new ArrayList<>();
        dfs(nums,target,new ArrayList<>(),0);
        return answer;
    }
}
