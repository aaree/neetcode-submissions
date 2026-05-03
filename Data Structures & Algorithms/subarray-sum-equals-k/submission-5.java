class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> map=new HashMap<>();
        map.put(0,1);
        int total=0;
        int cnt=0;
        for(int num:nums){
            total+=num;
            int opposite=total-k;
            if(map.containsKey(opposite)){
                cnt+=map.get(opposite);
            }
            map.merge(total,1,Integer::sum);
        }
        return cnt;
    }
}