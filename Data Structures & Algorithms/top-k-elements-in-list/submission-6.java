class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map=new HashMap<>();
        int[] ans=new int[k];
        List<Integer>[] temp=new List[nums.length+1];
        PriorityQueue<int[]> pq=new PriorityQueue<>((a,b)->{
            if (a[0]!=b[0]){
                return a[0]-b[0];
            }
            return a[1]-b[1];
        });
        for(int num: nums){
            map.merge(num,1,Integer::sum);
        }
        for(Map.Entry<Integer, Integer> e: map.entrySet()){
            int[] t={e.getValue(),e.getKey()};
            pq.offer(t);
        }
        while (pq.size()>k){
            pq.poll();
        }
        for(int i=0;i<k;i++){
            ans[i]=pq.poll()[1];
        }
        return ans;

    }
}
