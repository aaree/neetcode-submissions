class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int target=nums.length/3;
        List<Integer> ans=new ArrayList<>();
        Map<Integer, Integer> map=new HashMap<>();
        for (int num:nums){
            map.merge(num,1,Integer::sum);
        }
        for(Map.Entry<Integer, Integer> e: map.entrySet()){
            if (e.getValue()>target){
                ans.add(e.getKey());
            }
        }
        return ans;
    }
}